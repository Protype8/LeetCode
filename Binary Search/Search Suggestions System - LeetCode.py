class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        print(products)
        res = []
        l = 0
        r = len(products)-1
        for i in range(0,len(searchWord)):
            while(l < len(products) and searchWord[:i+1] != products[l][:i+1]):
                l += 1
            while(r > 0 and searchWord[:i+1] != products[r][:i+1]):
                r -= 1
            res.append(products[l:r+1][:3])
        return res
