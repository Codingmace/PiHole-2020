import re
a = "test string 1203-12.~fd38';" + "\nasn\nsdf\now23jd\noasjd\t\t\t\aasd"
result = re.sub('[\W_]+', ' ', a)
print(result)
