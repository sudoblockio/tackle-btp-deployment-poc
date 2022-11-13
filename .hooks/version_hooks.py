import semantic_version

from tackle import BaseHook, Field


class BumpVersionBlock(BaseHook):
    """Bump a semantic version."""
    hook_type: str = 'bump_version'

    version: str = Field(..., description="The current version.")
    version_bump: str = Field('patch')
    args: list = ['version']

    def exec(self) -> str:
        append_v = False
        if self.version.startswith('v'):
            append_v = True
            self.version = self.version[1:]

        v = semantic_version.Version(self.version)
        if self.version_bump == 'patch':
            new_v = v.next_patch()
        elif self.version_bump == 'minor':
            new_v = v.next_minor()
        elif self.version_bump == 'major':
            new_v = v.next_major()
        else:
            raise Exception(
                "The field 'version_bump' must be one of `major`, `minor`, or `patch`."
            )

        if append_v:
            new_v = 'v' + str(new_v)

        return new_v
