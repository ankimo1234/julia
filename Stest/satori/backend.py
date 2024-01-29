
import math

def get_julia(min_x,max_x,min_y,max_y,comp_const):
    box = {'x_axis':[],'y_axis':[],'color':[]}
    a = comp_const.real
    b = comp_const.imag
    
    # 変更可能------------------
    dots_num = 400
    j = 100
    # -------------------------

    N = 10**(len(str(dots_num))+1)
    for x in range(int(min_x*N),int(max_x*N),int((max_x-min_x)/dots_num*N)):
        for y in range(int(min_y*N),int(max_y*N),int((max_y-min_y)/dots_num*N)):
            xn = x
            yn = y
            for i in range(j): 
                xn1 = xn**2 - yn**2 + a*N*N
                yn1 = 2*xn*yn + b*N*N
                zz = complex(xn1,yn1)
                
                if abs(zz) > 2*N*N:
                    break
                elif math.isclose(xn/N,xn1/N/N,rel_tol=1/N*10) and math.isclose(yn/N,yn1/N/N,rel_tol=1/N*10):
                    box['x_axis'] += [x/N]
                    box['y_axis'] += [y/N]
                    box['color'] += [(1,1,1-1/j*i)]
                    break
                elif i == j-1:
                    box['x_axis'] += [x/N]
                    box['y_axis'] += [y/N]
                    box['color'] += [(1,1,1-1/j*i)]
                    break
                xn = xn1/N
                yn = yn1/N
    return box