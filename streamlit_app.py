import streamlit as st
from decimal import Decimal
import pandas as pd
import numpy as np
#business logic
class DocCompiler():
    def __init__(self):
        self.projects = []
        self.projectIndex= 0
    def push(self, _a):
        self.projects.append(_a)
        self.projectIndex += 1

class Goal():
    def __init__(self, name, description, primaryObjective):
        self.name = name
        self.description = description
        if name == primaryObjective:
            self.primary = True
            self.goalIndex = 0
        if primaryObjective != name:
            self.primary = False
            #search the secret vault for a name matching primary objective
            #return that index into goalIndex and push this gaol to the correct Vault
        
class Form():
	def __init__(self):
		self.goal = ''
		self.subGoals = []
		self.goalIndex = 0
		self.assets = []
		self.info = []
	def setGoal(self, text):
		self.goal = text
	
# Tests
## goal instantiation
f = Goal('UHPSC', 'the universal human processing and strategic conjugation form', 'UHPSC')
print(f.goalIndex)
## project Compilation
D = DocCompiler()
D.push(f)
print(D.projects[0].name)


#webpage
st.title("SPIRE")
st.write("Systematic Protection Information Resource Encapuslator")

arr1 = ["Procedure"]
arr2 = []
df1 = pd.DataFrame(arr2, columns=(arr1))
my_table1 = st.table(df1)
index1 = 0
x1 = st.text_input('Add Step')
update1 = st.button('update')
def updater1():
     global index1
     arr2.append([x1])
     st.write({index1})
     my_table1.add_rows(arr2[index1])
     index1 += 1
     st.write({index1})
     update1 = False
if update1 == True:
     updater1()

st.write({index1})
df2 = pd.DataFrame( columns=("Assets", "Information"))

my_table2 = st.table(df2)