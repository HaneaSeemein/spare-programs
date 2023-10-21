class leaf:
    def __init__(self,data,children,parent):    
        self.data = data
        self.children = children
        self.parent = parent

def createleaf(port,path,parent):
    to = []
    for route in path:
        if(route[0]==port):
            to.append(route[1])
    return leaf(port,to,parent)

def backtrack(backfrm,thepath,frmflight):
    while(backfrm.data!=frmflight):
        thepath.insert(0,backfrm.data)
        backfrm = backfrm.parent
    thepath.insert(0,frmflight)
    return thepath

def shortestflight(frmflight,destination,path):
    stages = []
    headstation = createleaf(frmflight,path,None)
    stages.append(headstation)
    for stations in stages:
     for tostation in stations.children:
        if(tostation==destination):
            print(tostation+"=="+str(stations.data))
            return backtrack(stations,[destination],frmflight)
        else:
            stages.append(createleaf(tostation,path,stations))
            print(tostation+"--"+str(stations.data))
data = [
	["Russian Federation","New Zealand"],
	["Colombia","Ireland"],
	["South Korea","United States"],
	["India","Mexico"],
	["Australia","Netherlands"],
	["India","Turkey"],
	["China","Peru"],
	["Poland","Singapore"],
	["Spain","Germany"],
	["South Korea","Indonesia"],
	["South Africa","Russian Federation"],
	["Turkey","Ireland"],
	["New Zealand","Ukraine"],
	["Canada","New Zealand"],
	["Vietnam","Russian Federation"],
	["Mexico","Canada"],
	["Belgium","Ukraine"],
	["Turkey","India"],
	["Belgium","United Kingdom"],
	["United States","Mexico"],
	["Italy","Indonesia"],
	["Costa Rica","Netherlands"],
	["Norway","Costa Rica"],
	["Brazil","South Korea"],
	["United Kingdom","South Africa"],
	["United States","Sweden"],
	["Norway","Brazil"],
	["South Korea","United Kingdom"],
	["Indonesia","Nigeria"],
	["New Zealand","United States"],
	["South Africa","Canada"],
	["Pakistan","Pakistan"],
	["United States","France"],
	["Russian Federation","Norway"],
	["Ireland","Ireland"],
	["Spain","Italy"],
	["Poland","Brazil"],
	["Sweden","France"],
	["Poland","Peru"],
	["Peru","Colombia"],
	["India","Chile"],
	["Russian Federation","Netherlands"],
	["Austria","Canada"],
	["Austria","Vietnam"],
	["Colombia","Spain"],
	["United States","Pakistan"],
	["France","South Africa"],
	["Peru","Australia"],
	["China","South Africa"],
	["Nigeria","Australia"],
	["Poland","Belgium"],
	["Belgium","South Africa"],
	["Italy","Canada"],
	["Norway","Nigeria"],
	["Spain","India"],
	["Costa Rica","Poland"],
	["Spain","Philippines"],
	["Italy","Austria"],
	["South Korea","Indonesia"],
	["Belgium","New Zealand"],
	["Russian Federation","Brazil"],
	["Austria","Sweden"],
	["Italy","Netherlands"],
	["Nigeria","Ukraine"],
	["Singapore","Italy"],
	["Belgium","Turkey"],
	["Sweden","Pakistan"],
	["United States","Netherlands"],
	["Sweden","Belgium"],
	["Nigeria","Singapore"],
	["Spain","Chile"],
	["Russian Federation","Philippines"],
	["Singapore","Ukraine"],
	["Pakistan","Vietnam"],
	["Chile","Indonesia"],
	["Chile","South Korea"],
	["United Kingdom","South Africa"],
	["Mexico","Pakistan"],
	["United Kingdom","Philippines"],
	["Australia","Brazil"],
	["United States","France"],
	["United Kingdom","Costa Rica"],
	["Sweden","Colombia"],
	["Vietnam","Ireland"],
	["Ireland","Indonesia"],
	["Ireland","Ukraine"],
	["Belgium","Ireland"],
	["Costa Rica","Belgium"],
	["Costa Rica","Nigeria"],
	["China","Netherlands"],
	["Ireland","Austria"],
	["United Kingdom","China"],
	["Peru","China"],
	["Austria","Singapore"],
	["China","Vietnam"],
	["Spain","Belgium"],
	["New Zealand","Russian Federation"],
	["Costa Rica","India"],
	["Costa Rica","Russian Federation"],
	["Belgium","Vietnam"]
]
print(shortestflight('Austria','Peru',data))