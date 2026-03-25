visitors = set()

def add_visitor(name):
    visitors.add(name)

def total_visitors():
    print("Unique Visitors:", len(visitors))
