import rospy
from costmap_query.srv import ComputeCost, ComputeCostRequest, ComputeCostResponse
from std_msgs.msg import Float32

name = "compute_cost"
rospy.wait_for_service(name)
sp = rospy.ServiceProxy(name, ComputeCost)
ret = sp([-0.8, 0], [0, 0])
print(ret)

