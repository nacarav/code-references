/**
 * Models a sphere in 3-d space
 * @author Nick Caravaggio
 */
public class Sphere implements GeometricSolid
{
    private double radius;
   

    /**
     * Constructor for objects of class Sphere
     * @param radius the radius of this Sphere
     */
    public Sphere(double radius)
    {
        this.radius =  radius;
    }
    
    /**
     * Gets the radius of this Sphere
     * @return the radius of this Sphere
     */
    public double getRadius()
    {
        return radius;
    }
    
    /**
     * Sets the the radius of this Sphere
     * @param newRadius the radius of this Sphere
     */
    public void setRadius(double newRadius)
    {
        radius = newRadius;
    }
    
     /**
     * Returns volume of cylinder.
     * @return theVolume the volume.
     */
    public double volume()
    {
       double theVolume;
       theVolume = (((4 * Math.PI) / 3) * radius * radius * radius);
       return theVolume;
    }

     
}