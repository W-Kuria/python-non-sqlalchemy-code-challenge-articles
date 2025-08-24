from classes.many_to_many import Author, Magazine, Article
import ipdb

a1 = Author("Alice")
a2 = Author("Bob")

m1 = Magazine("TechLife", "Technology")
m2 = Magazine("HealthMag", "Wellness")

a1.add_article(m1, "AI in 2025")
a1.add_article(m2, "Mindful Living")
a2.add_article(m1, "Quantum Computing")
a1.add_article(m1, "Future of Robotics")
a1.add_article(m1, "VR and Society")

# don't remove this line, it's for debugging!
ipdb.set_trace()
