class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        e = []
        for email in emails:
            name,domain = email.split("@")
            name = name.replace(".","").split("+")[0]
            if(name+"@"+domain not in e):
                e.append(name+"@"+domain)
        return len(e)
