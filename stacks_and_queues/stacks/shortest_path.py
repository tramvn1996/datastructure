#normalize path name
#we're splitting the string into an array
#the possible elements in the path now can be: names, '..'
#we iterate through the array:
#if the element is "..", then we have these cases:
#1. the beginning of the path name is "..", which points to the parent dir of the current location
#2. the last item is also a "..", then it's like ../../../
#If it is these 2 cases, then we just add .. to the array

#else, which is the case that the ".." is not at the beginning of the path, or p
#preceeded by a "..", which means it's preceeded by a name
# if a name followed "..", like name/../, then we can shorten the path to/
#if it's /.. -> false path

#else, if it's a name, add it to the path

def shortest_path(path):
    if not path:
        raise ValueError("the path cannot be blank")

    path_name =[] #use list as a stack

    if path[0]=='/':
        path_name.append('/')

    for token in (token for token in path.split('/') if token not in['','.']):
        if token == '..':
            if not path_name or path_name[-1]=='..':
                path_name.append(token)
            else:
                if path_name[-1]=='/':
                    raise ValueError('Path error')
                path_name.pop() #return to the parent folder
        else:
            path_name.append(token)

    result = '/'.join(path_name)

    return result[result.startswith('//'):] #avoid starting with //

print(shortest_path('/sr/name/se/../na'))

#time complexity is O(n)
