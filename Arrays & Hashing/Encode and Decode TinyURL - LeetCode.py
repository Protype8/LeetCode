import string
import random
class Codec:
    long_to_short = {}
    short_to_long = {}
    def encode(self, longUrl: str) -> str:
        if(longUrl in self.long_to_short):
            return url_dict[longUrl]
        else:
            code = "".join(random.choices(string.ascii_letters+string.digits,k=8))
            self.long_to_short[longUrl] = code
            self.short_to_long[code] = longUrl
            return code
    def decode(self, shortUrl: str) -> str:
        return self.short_to_long[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
