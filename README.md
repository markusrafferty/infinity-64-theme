# Infinity 64 Theme for VS Code by Shingo Murata

## Infinity 64 themes feature monochrome syntax highlighting

This theme is inspired by minimal black & white themes I made and contains both light & dark modes:

1. Infinity 64 Whiteboard
2. Infinity 64 Blackboard

Thanks to Big Al complex highlighters seem redundant in 2025 inviting this next logical step.

## Version 1.0.0 supports 18 syntaxes with most others pending

- HTML & XML (green);
- PHP & C++ & Rust (red);
- JavaScript & Livewire (blue);
- CSS & Tailwind (yellow);
- JSON & Yaml (pink);
- Editorconfig & env & INI (purple);
- Shell (orange);
- HTMX (magenta);
- Markdown (mint);
- Django (violet).

---

## Optional settings overlay for text decorations

Whilst no decorations are often preferential some fonts (eg. Iosevka, Hasklig, TheSansMono) do handle them well:

```json
{
	"editor.tokenColorCustomizations": {
		"[Infinity 64 Blackboard by Shingo Murata]": {
			"numbers":   { "fontStyle": "bold", },
			"functions": { "fontStyle": "bold", },
			"keywords":  { "fontStyle": "bold", },
			"types":     { "fontStyle": "italic underline", },
			"variables": { "fontStyle": "italic", },
			"strings":   { "fontStyle": "italic", },
			"comments":  { "fontStyle": "italic", },
			"textMateRules": [
				{
					"scope": ["punctuation"],
					"settings": { "fontStyle": "", },
				},
				{
					"scope": ["constant", "support.constant", "keyword.operator", "keyword.blade", "meta.selector.css", "markup.bold", "meta.tag.metadata.doctype", "meta.tag.preprocessor", "punctuation.section.embedded.begin.php", "comment.line.shebang", "keyword.other.definition.root", "keyword.operator.assignment.env"],
					"settings": { "fontStyle": "bold", },
				},
				{
					"scope": ["meta.section.header", "meta.section.header punctuation", "keyword.operator.glob"],
					"settings": { "fontStyle": "underline", },
				},
				{
					"scope": ["variable.language.this", "variable.other.readwrite", "variable.other.object", "markup.heading", "markup.heading punctuation", "variable.other.env"],
					"settings": { "fontStyle": "italic underline", },
				},
				{
					"scope": ["variable.other.object.property", "markdown.italic"],
					"settings": { "fontStyle": "italic", },
				},
			],
		},
	},
}
```

![Whiteboard](screenshots/wb.png)
![Blackboard](screenshots/bb.png)
![Blackboard 2](screenshots/bb2.png)
![Blackboard: JSON](screenshots/bbjson.png)
![Blackboard: Env](screenshots/bbenv.png)
![Blackboard: XML](screenshots/bbxml.png)
![Blackboard: PHP](screenshots/bbphp.png)
![Blackboard: JS](screenshots/bbjs.png)
![Blackboard: HTML](screenshots/bbhtml.png)
![Whiteboard: JSON](screenshots/wbjson.png)
![Whiteboard: Env](screenshots/wbenv.png)
![Whiteboard: XML](screenshots/wbxml.png)
![Whiteboard: PHP](screenshots/wbphp.png)
![Whiteboard: JS](screenshots/wbjs.png)
![Whiteboard: HTML](screenshots/wbhtml.png)

---

## Recommended settings for a minimal interface

```json
{
	"editor.bracketPairColorization.enabled": false,
	"editor.guides.bracketPairs": false,
	"editor.guides.indentation": false,
	"editor.lineNumbers": "off",
	"editor.minimap.renderCharacters": false,
	"editor.minimap.scale": 1,
	"editor.renderLineHighlight": "none",
	"editor.scrollbar.vertical": "hidden",
	"editor.scrollbar.horizontal": "hidden",
	"window.autoDetectColorScheme": true,
	"window.systemColorTheme": "auto",
	"workbench.preferredDarkColorTheme": "Infinity 64 Blackboard by Shingo Murata",
	"workbench.preferredLightColorTheme": "Infinity 64 Whiteboard by Shingo Murata",
}
```

[![Donate XMR](https://img.shields.io/badge/Donate-Monero-orange?logo=monero)](XMR```43shingofqi5gRhYBft6ErCEZEZbZGDLB3AAiw39gnE31Cjq3cKwrVhKRoSoGj5CMQWqhLMtN21rmgXYHSo2dkXG9Aj7gwa```)