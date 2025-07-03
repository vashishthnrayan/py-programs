student_data={'id1':
    {'name':['sara']
     ,'class':['7']
     ,'subject_integration':['maths,english,scince']
    },
    'id2':
     {'name':['john']
     ,'class':['7']
     ,'subject_integration':['maths,english,scince']
    },
    'id3':
    { 'name':['sara']
     ,'class':['7']
     ,'subject_integration':['maths,english,scince']
    },
    'id4':
    {'name':['Vasu']
    ,'class':['7']
    ,'subject_integration':['maths,english,scince']
    },
}

result = {}

for key, value in student_data.items():
    if value not in result.values():
        result[key] = value
    
print(result)
