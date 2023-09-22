#find the target product in the list and return a list of indices of all occurrences of the product if found,or an empty list if the product is not found 

def linearSearchProduct(productList, targetproduct):
  indices = []
  for index, product in enumerate(productList):
    if product == targetproduct:
      indices.append(index)


  return indices


#Example usage:
products =["bat", "boot","loafer","bat", "sandals","bat"]
target ="bat"
target2 ='apple'
result = linearSearchProduct(products, target)
print(result)