class Stack:
    def __init__(self):
        self.notes = []
    def isEmpty(self):
        return self.notes == []
    def add(self, elem):
        self.notes.append(elem)
    def length(self):
        return len(self.notes)             
    def peek(self):
        return self.notes[-1]
    def remove(self):
        duration = self.notes.pop()
        note = self.notes.pop()
        return (note, duration)
    def firstElement(self):
        return self.notes[0]
        
        

class Queue:
    def __init__(self):
        self.notes = []
    def isEmpty(self):
        return self.notes == []
    def add(self, elem):
        self.notes.append(elem)
    def length(self):
        return len(self.notes)  
    def peek(self):
        return self.notes[0] 
    def remove(self):
        return self.notes.pop(0)
    