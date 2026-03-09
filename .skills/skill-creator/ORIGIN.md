# Upstream Provenance: skill-creator

- Source repository: https://github.com/anthropics/skills
- Subdirectory: skills/skill-creator
- Installed at: 2026-03-09T03:41:35Z (UTC)
- Installed by: main-assistant-agent-kinara (agent-b1574f99-be7c-4772-8db2-ea2b35b18d1a)
- Installed version: HEAD (b0cbd3d)
- Commit URL: https://github.com/anthropics/skills/commit/b0cbd3df1533b396d281a6886d5132f623393a9c
- Retrieval method: shallow clone (depth=1) and copy, no script execution
- License: see LICENSE.txt in this folder (from upstream)

## Update instructions
To refresh to the latest upstream HEAD:
1) git clone --depth 1 https://github.com/anthropics/skills /tmp/anthropics-skills
2) rsync -a /tmp/anthropics-skills/skills/skill-creator/ ./.skills/skill-creator/
3) rm -rf /tmp/anthropics-skills
4) Commit changes with a message noting the new upstream SHA.

To pin to a specific version, replace HEAD above with a specific commit and copy that tree.
