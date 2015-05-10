from numpy import *

def delta_y(A, B):
	return double(abs(A.tolist()[0][1] - B[1]))


def randCent(data_points, k):
    n = shape(data_points)[1]
    centroids = mat(zeros((k,n)))
    for j in range(n):
        minJ = min(data_points[:,j]) 
        rangeJ = float(max(data_points[:,j]) - minJ)
        centroids[:,j] = mat(minJ + rangeJ * random.rand(k,1))
    return centroids


def kMeans(data_points, k, createCent=randCent):
    m = shape(data_points)[0]
    clusterAssment = mat(zeros((m,2)))

    centroids = createCent(data_points, k)
    #print centroids
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):#for each data point assign it to the closest centroid
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = delta_y(centroids[j,:],data_points[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        #print centroids
        for cent in range(k):#recalculate centroids
            ptsInClust = data_points[nonzero(clusterAssment[:,0].A==cent)[0]]#get all the point in this cluster
            centroids[cent,:] = mean(ptsInClust, axis=0) #assign centroid to mean 
    return clusterAssment




data_points = [
			[1,40],[2,32],[3,38],[4,37],[5,36],
			[6,30],[7,29],[8,28],[9,27], 
			[10,30],[11,29],[12,28],[13,27],
			[14,20],[15,19],[16,18],[17,17],
			[18,20],[19,19],[20,18],[21,17]
		]

data_points = array(data_points)
print kMeans(data_points, 5)