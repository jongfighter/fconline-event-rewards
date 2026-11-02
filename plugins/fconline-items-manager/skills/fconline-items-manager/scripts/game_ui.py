"""FC ONLINE screen capture and one observed UI action per call. No elevation."""
import argparse
import ctypes
import json
import math
import sys
import time
from ctypes import wintypes as w
from pathlib import Path


class Mouse(ctypes.Structure):
    _fields_ = [('dx', w.LONG), ('dy', w.LONG), ('mouseData', w.DWORD),
                ('dwFlags', w.DWORD), ('time', w.DWORD), ('extra', ctypes.c_size_t)]


class Keyboard(ctypes.Structure):
    _fields_ = [('vk', w.WORD), ('scan', w.WORD), ('flags', w.DWORD),
                ('time', w.DWORD), ('extra', ctypes.c_size_t)]


class InputData(ctypes.Union):
    _fields_ = [('mouse', Mouse), ('key', Keyboard)]


class Input(ctypes.Structure):
    _fields_ = [('type', w.DWORD), ('data', InputData)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', nargs='?', default='{"action":"capture"}')
    parser.add_argument('--output-dir', type=Path,
                        default=Path.home() / 'FCOnline' / 'skill-ui-captures')
    args = parser.parse_args()
    command = json.loads(args.command)
    action = command.get('action')
    if action not in {'capture', 'focus', 'move', 'click', 'wheel', 'escape', 'number'}:
        raise ValueError('Unsupported action; send one JSON object per call')
    delay = float(command.get('wait', 1.0))
    if not math.isfinite(delay) or not 0 <= delay <= 10:
        raise ValueError('wait must be between 0 and 10 seconds')
    if action == 'number':
        value = str(command.get('value', ''))
        if not value.isascii() or not value.isdigit() or len(value) > 6:
            raise ValueError('Only 1 to 6 ASCII digits are supported')
    count = int(command.get('count', 1))
    amount = int(command.get('amount', -120))
    if action == 'wheel' and (not 1 <= count <= 60 or not 1 <= abs(amount) <= 1200):
        raise ValueError('Invalid wheel count or amount')

    u = ctypes.WinDLL('user32', use_last_error=True)
    u.SetThreadDpiAwarenessContext.argtypes = [ctypes.c_void_p]
    u.SetThreadDpiAwarenessContext(ctypes.c_void_p(-4))
    u.FindWindowW.argtypes = [w.LPCWSTR, w.LPCWSTR]
    u.FindWindowW.restype = w.HWND
    u.GetForegroundWindow.restype = w.HWND
    u.SetForegroundWindow.argtypes = [w.HWND]
    u.GetClientRect.argtypes = [w.HWND, ctypes.POINTER(w.RECT)]
    u.ClientToScreen.argtypes = [w.HWND, ctypes.POINTER(w.POINT)]
    u.IsIconic.argtypes = [w.HWND]
    u.IsWindowVisible.argtypes = [w.HWND]
    u.WindowFromPoint.argtypes = [w.POINT]
    u.WindowFromPoint.restype = w.HWND
    u.GetAncestor.argtypes = [w.HWND, w.UINT]
    u.GetAncestor.restype = w.HWND
    u.GetWindowLongW.argtypes = [w.HWND, ctypes.c_int]
    u.SendInput.argtypes = [w.UINT, ctypes.POINTER(Input), ctypes.c_int]
    u.SendInput.restype = w.UINT

    handle = u.FindWindowW(None, 'FC ONLINE')
    if not handle:
        raise RuntimeError('FC ONLINE window missing')
    if u.IsIconic(handle) or not u.IsWindowVisible(handle):
        raise RuntimeError('Game is minimized or hidden; inspect/restore it first')
    origin, size = w.POINT(), w.RECT()
    if not u.ClientToScreen(handle, ctypes.byref(origin)) or not u.GetClientRect(handle, ctypes.byref(size)):
        raise ctypes.WinError(ctypes.get_last_error())
    if size.right <= 0 or size.bottom <= 0:
        raise RuntimeError('Game client has no drawable area')

    def send(event):
        if u.SendInput(1, ctypes.byref(event), ctypes.sizeof(Input)) != 1:
            raise RuntimeError('SendInput blocked; check Windows integrity level and permission')

    def mouse_click():
        event = Input()
        event.data.mouse.dwFlags = 2
        send(event)
        try:
            time.sleep(.1)
        finally:
            event.data.mouse.dwFlags = 4
            send(event)

    def foreground():
        if u.GetForegroundWindow() != handle:
            raise RuntimeError('Game lost foreground; refusing input')

    if action != 'capture':
        if u.GetForegroundWindow() != handle:
            u.SetForegroundWindow(handle)
            time.sleep(.2)
        if u.GetForegroundWindow() != handle:
            # Only click a verified, visible native title bar belonging to this game.
            point = w.POINT(origin.x + 80, origin.y - 10)
            hit = u.WindowFromPoint(point)
            if (u.GetWindowLongW(handle, -16) & 0x00C00000) == 0x00C00000 and u.GetAncestor(hit, 2) == handle:
                u.SetCursorPos(point.x, point.y)
                mouse_click()
                time.sleep(.3)
        foreground()

    if action in {'move', 'click', 'wheel'}:
        x, y = float(command['x']), float(command['y'])
        if not (math.isfinite(x) and math.isfinite(y) and 0 <= x < 1600 and 0 <= y < size.bottom * 1600 / size.right):
            raise ValueError('Coordinates outside the normalized game client')
        px = min(size.right - 1, round(x * size.right / 1600)) + origin.x
        py = min(size.bottom - 1, round(y * size.right / 1600)) + origin.y
        hit = u.WindowFromPoint(w.POINT(px, py))
        if u.GetAncestor(hit, 2) != handle:
            raise RuntimeError('Observed game position is covered by another window')
        if not u.SetCursorPos(px, py):
            raise ctypes.WinError(ctypes.get_last_error())
        time.sleep(.2)
        foreground()
        if action == 'click':
            mouse_click()
        elif action == 'wheel':
            for _ in range(count):
                foreground()
                event = Input()
                event.data.mouse.dwFlags = 0x0800
                event.data.mouse.mouseData = amount & 0xffffffff
                send(event)
                time.sleep(.12)
    elif action in {'escape', 'number'}:
        def key(vk, up=False):
            if not up:
                foreground()
            event = Input()
            event.type = 1
            event.data.key.vk = vk
            event.data.key.flags = 2 if up else 0
            send(event)
            time.sleep(.06)

        def press(vk):
            key(vk)
            try:
                time.sleep(.04)
            finally:
                key(vk, True)

        if action == 'escape':
            press(27)
        else:
            key(17)
            try:
                press(65)
            finally:
                key(17, True)
            for digit in value:
                press(ord(digit))

    time.sleep(delay)
    # A fresh path for every successful call prevents stale screenshots after failures.
    from PIL import ImageGrab
    args.output_dir.mkdir(parents=True, exist_ok=True)
    stamp = str(time.time_ns())
    full_path = args.output_dir / (stamp + '-full.png')
    image_path = args.output_dir / (stamp + '.png')
    frame = ImageGrab.grab(bbox=(origin.x, origin.y, origin.x + size.right, origin.y + size.bottom), all_screens=True)
    frame.save(full_path)
    frame = frame.resize((1600, max(1, round(size.bottom * 1600 / size.right))))
    frame.save(image_path)
    print(json.dumps({'ok': True, 'action': action, 'game_foreground': u.GetForegroundWindow() == handle,
                      'elevated': bool(ctypes.windll.shell32.IsUserAnAdmin()),
                      'client_size': [size.right, size.bottom], 'coordinate_width': 1600,
                      'image': str(image_path), 'full_image': str(full_path)}))


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(json.dumps({'ok': False, 'error': str(error)}))
        sys.exit(1)
