numbers = []
list(map(
    lambda number: numbers.append( number ),
    [ 1,2,4,5,6,7,7 ]
))
def testingYes( value ):
    print( value )
    return value

def testingNo( value = None ):
    print( value )
    return value

man = {
    'name': 'carlos'
}
name = {
    True: lambda: testingYes(man['name']),
    False: lambda: testingNo(man['last_name'])
}[ not 'last_name' in man ]()
print( name )