from scipy import *
import matplotlib.pyplot as plt
class sondenplatz:

    def __init__(self,Name,centre,radius,points_per_meter):
        acc=points_per_meter*radius
        self.name=Name
        self.type="Sondenplatz"
        self.position_tuple=centre
        self.radius=radius
        delta_angle=2*pi/acc
        delta_radius=radius/acc
        self.area=zeros([acc,acc,2])
        theta=(arange(acc)+1)[:,newaxis]*2*pi/acc
        r=(arange(acc)+1)[newaxis,:]*radius/acc
        self.area[:,:,0]=r*cos(theta)+self.position_tuple[0]
        self.area[:,:,1]=r*sin(theta)+self.position_tuple[1]
        #print shape(self.area)
        # for radius_index in arange(acc):
            # for angle_index in arange(acc):
                # r=delta_radius*(radius_index+1)
                # theta=delta_angle*(angle_index+1)
                # self.area[radius_index,angle_index,0]=r*cos(theta)+self.position_tuple[0]
                # self.area[radius_index,angle_index,1]=r*sin(theta)+self.position_tuple[1]
        #print shape(r), shape(theta), shape(r*cos(theta)),shape(r*sin(theta))
        #print max(ravel(r*cos(theta)))-min(ravel(r*cos(theta)))
        #print max(ravel(r*sin(theta)))-min(ravel(r*sin(theta)))
        
        #fig=plt.figure()
        #plt.plot((r*cos(theta))[:,acc-1],(r*sin(theta))[:,acc-1])
        #plt.show()
        #plt.close(fig)

class pipeline:  
    """
    class Pipeline
    
    Methods:
    __init__(Name,Points_of_direction_change)
    
    save(filename)
    
    instance variable:
    
    self.Name
    Name of the pipeline
   
    self.Endpoints
    self.Number_of_sections
    self.section_lenghts
    self.course
    self.lenght
    """
    
    
    def __init__(self,name,Points_of_direction_change,radius,lenght,points_per_metre=3.):
        """
        def __init__(self,Name, Points_of_direction_change,acc=10**6)

        Creates a Pipeline object.

        Parameters:
        Name
        The name of the pipeline.

        Points_of_direction_change
        Array  of 2D-points (Dimensions [n,2]), describing a pipeline as an object of connected straight lines.
        Each point of the array is a point were the pipeline changes direction.

        Example  
                  c________________ 
                 /  
        a______b/

        Points_of_direction_change[0,0] = a_x
        Points_of_direction_change[0,1] = a_y

        Points_of_direction_change[1,0] = b_x
        Points_of_direction_change[1,1] = b_y

        Points_of_direction_change[2,0] = c_x
        Points_of_direction_change[2,1] = c_y

        acc
        Number of datapoints between Points were the direction of the pipeline changes.

        Returns:
        Pipeline object
        """    
        self.endpoints=Points_of_direction_change
        self.name=name
        self.number_of_sections = len(Points_of_direction_change[:,0])-1

        self.radius=radius

        self.type="Leitung"

        self.section_lenghts=zeros(self.number_of_sections)
        for section_index in arange(self.number_of_sections):
            self.section_lenghts[section_index]=sqrt((self.endpoints[section_index+1,0]-self.endpoints[section_index,0])**2+(self.endpoints[section_index+1,1]-self.endpoints[section_index,1])**2)
            
        max_lenght=max(self.section_lenghts)
        
        acc=ceil(max_lenght*points_per_metre)
        
        self.course=zeros([self.number_of_sections,acc+1,2])
        for section_index in arange(self.number_of_sections):
              #print shape(self.course[section_index,:,0])
              self.course[section_index,:,0]=self.endpoints[section_index,0]+arange(acc+1)*(self.endpoints[section_index+1,0]-self.endpoints[section_index,0])/(acc+1)
              self.course[section_index,:,1]=self.endpoints[section_index,1]+arange(acc+1)*(self.endpoints[section_index+1,1]-self.endpoints[section_index,1])/(acc+1)  
        
        if lenght==0:
            self.lenght=0.0
            for i in arange(self.number_of_sections):
                self.lenght=self.lenght+self.section_lenghts[i]
        else:
            self.lenght=lenght
        # determining the area covered by the pipeline
        # self.course is our centerline

        # determine our number of points acc pendicular to the centerline
        acc=ceil(radius*points_per_metre)
        
        pendicular_distance=arange(2*acc+1)*radius/(2*acc)
        pendicular_distance=pendicular_distance-pendicular_distance[-1]/2.
        # adding an additional index:
        # self.area[i,j,k,l]
        # i section 
        # j centerline 
        # k point pendicular to the centerline	
        #	0    => point in a pendicular distance of -radius under the centerline
        #   acc  =>point in a pendicular distance of radius over the centerline
        #              index acc, point in distance +r
        #               x 
        #               |  		
        #               |  
        #--------------------- centerline
        #               |
        #               |
        #               x
        #       index acc, point in distance -r
        #
        #building the shape of the array
        s1,s2,s3=shape(self.course)
        self.area=zeros([s1*s2,2*acc+1,s3])
        for section_index in arange(len(self.course[:,0,0])):
            # construct normal vector
            # (x2-x1, y2-y1) tangent vektor
            delta_x=self.endpoints[section_index+1,0]-self.endpoints[section_index,0]
            delta_y=self.endpoints[section_index+1,1]-self.endpoints[section_index,1]
            n1=+delta_y/sqrt(delta_x**2+delta_y**2)
            n2=-delta_x/sqrt(delta_x**2+delta_y**2)
            n=asarray([n1,n2])
            for d_index in arange(len(pendicular_distance)):
                array=n*pendicular_distance[d_index] 
                self.area[section_index*(s2):(section_index+1)*s2,d_index,:]=self.course[section_index,:,:]+array

         

class windturbine:  
    """
    class windturbine
    Base assumption: Rotor blade can be treated like an trapez
    Methods:
    __init__(name,type,rotor_blade_date,hub_data,wind_data)

    rotor_blade_date=[rotor_blade_lenght,rotor_blade_width_tip,rotor_blade_width_base,rotor_blade_mass]
    rated_speed_data=[rotor_rated_speed_tuple,rotor_wind_speed_tuple]
    hub_data=[hub_radius,hub_height]
    wind_data=[wind_distribution,weibull_scale,weibull_shape,]
    instance variable:
    
    self.name
    self.type
    self.position_tuple
    
    self.rotor_blade_lenght
    self.rotor_blade_width_tip
    self.rotor_blade_width_base
    self.rotor_blade_area
    self.rotor_blade_mass
    
    self.hub_radius
    self.hub_height
    
    self.rotor_rated_speed_tuple
    self.rotor_wind_speed_tuple
    
    self.wind_distribution
    self.weibull_scale
    self.weibull_shape
    """
    def __init__(self,name,type,position_tuple,rotor_blade_data,rated_speed_data,hub_data,wind_data):
        rotor_blade_lenght,rotor_blade_width_tip,rotor_blade_width_base,rotor_blade_mass=rotor_blade_data
        rotor_rated_speed_tuple,rotor_wind_speed_tuple=rated_speed_data
        hub_radius,hub_height=hub_data
        wind_distribution,weibull_scale,weibull_shape=wind_data
        
        self.name=name
        self.type=type
        self.position_tuple=position_tuple
        
        self.rotor_blade_lenght=rotor_blade_lenght
        self.rotor_blade_width_tip=rotor_blade_width_tip
        self.rotor_blade_width_base=rotor_blade_width_base
        self.rotor_blade_area=rotor_blade_area=0.5*rotor_blade_lenght*(rotor_blade_width_tip+rotor_blade_width_base)
        self.rotor_blade_mass=rotor_blade_mass
        
        self.hub_radius=hub_radius
        self.hub_height=hub_height
        
        self.rotor_rated_speed_tuple=rotor_rated_speed_tuple
        self.rotor_wind_speed_tuple=rotor_wind_speed_tuple
        
        self.wind_distribution=wind_distribution
        self.weibull_scale=weibull_scale
        self.weibull_shape=weibull_shape
        
        self.wind_cumulative_probabilities=zeros(len(self.wind_distribution))
        self.wind_cumulative_probabilities[0]=self.wind_distribution[0]
        for cum_prob_index in arange(len(self.wind_distribution)-1):
            self.wind_cumulative_probabilities[cum_prob_index+1]=self.wind_cumulative_probabilities[cum_prob_index ]+self.wind_distribution[cum_prob_index+1]    
