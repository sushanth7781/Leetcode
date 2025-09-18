class Solution:
    def simplifyPath(self, path: str) -> str:
        s=[]
        p=path.split("/")
        for part in p:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if s:
                    s.pop()
            else:
              s.append(part)
        return "/" + "/".join(s)