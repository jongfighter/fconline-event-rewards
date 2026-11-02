import { readFile } from "node:fs/promises"
import { fileURLToPath } from "node:url"
import { Plugin, Skill } from "@opencode/plugin"

const SKILL_ID = "fconline-items-manager"
const SKILL_PATH = fileURLToPath(new URL(`../skills/${SKILL_ID}/SKILL.md`, import.meta.url))

function scalar(key: string, raw: string) {
  const value = raw.trim()
  if (/^[>|]/.test(value)) throw new Error(`${SKILL_PATH}: frontmatter "${key}" must be a single-line scalar`)
  if (value.startsWith('"')) {
    try {
      return JSON.parse(value) as string
    } catch (cause) {
      throw new Error(`${SKILL_PATH}: frontmatter "${key}" is not a valid double-quoted string`, { cause })
    }
  }
  if (value.startsWith("'") && value.endsWith("'") && value.length > 1) return value.slice(1, -1).replaceAll("''", "'")
  return value
}

function parse(source: string) {
  const frontmatter = /^\uFEFF?---\r?\n([\s\S]*?)\r?\n---[ \t]*(?:\r?\n|$)/.exec(source)
  if (!frontmatter) throw new Error(`${SKILL_PATH}: missing YAML frontmatter`)
  const field = (key: string) => {
    const line = new RegExp(`^${key}:(.*)$`, "m").exec(frontmatter[1])
    return line ? scalar(key, line[1]) : undefined
  }
  const description = field("description")
  if (!description) throw new Error(`${SKILL_PATH}: frontmatter has no description`)
  return {
    name: field("name") || SKILL_ID,
    description,
    content: source.slice(frontmatter[0].length),
  }
}

export default Plugin.define({
  id: SKILL_ID,
  async setup(ctx) {
    const skill = parse(await readFile(SKILL_PATH, "utf8"))
    await ctx.skill.transform((editor) => {
      editor.add({
        id: Skill.ID.make(SKILL_ID),
        name: Skill.Name.make(skill.name),
        description: skill.description,
        path: Skill.Info.fields.path.make(SKILL_PATH),
        content: skill.content,
      })
    })
  },
})
