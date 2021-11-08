import xml.dom.minidom
import time

start_time = time.time()
doc = xml.dom.minidom.parse('0355619.xml')
doc.normalize()
node1 = doc.getElementsByTagName('roster')
print(node1)
print("name=" + node1[0].nodeName)
print("attr="+node1[0].getAttribute("totalCost"))
print(doc.firstChild.tagName)

print("--- %s seconds ---" % (time.time() - start_time))
