def f(ls):
    x1,x2,x3 = ls
    result = 100*(x2-x1**2)**2+(1-x1)**2+100*(x3-x2**2)**2+(1-x2)**2
    return result
start_points = []
start_points.append([0,0,0])
start_points.append([10,-3,2])
start_points.append([1,1.5,9])
start_points.append([2,1,0])
start_points.append([-2,0,2])
obj_value=[]
resol=[]
for i in start_points:
    result = scipy.optimize.minimize(f,i, method = "BFGS")
    resol.append(result.x)
    obj_value.append(result.fun)

opt_value = obj_value[0]
opt_resol = resol[0]
for i in range(1,len(obj_value)):
    if obj_value[i] < opt_value:
        opt_value = obj_value[i]
        opt_sol = resol[i]

print (opt_sol)
