#-- self test to see what is on the classpath
from java.lang import ClassLoader
cl = ClassLoader.getSystemClassLoader()
paths = map(lambda url: url.getFile(), cl.getURLs())
print paths
#----- try to access an owltools class
from owltools.graph import OWLGraphWrapper
print OWLGraphWrapper.getClass().getName()
