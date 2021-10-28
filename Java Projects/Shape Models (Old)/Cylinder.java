/**
 * Models a Cylinder
 * @author Nick Caravaggio
 * @version Fall 2018
 */
public class Cylinder implements GeometricSolid
{
    private double radius;
    private double height;

    /**
     * Constructor for objects of class Cylinder
     * @param radius the radius of the Cylinder
     * @param height the height of this Cylinder
     */
    public Cylinder(double radius, double height)
    {
        this.radius = radius;
        this.height = height;
    }
    
    /**
     * Gets the radius of this Cylinder
     * @return the radius of the Cylinder
     */
    public double getRadius()
    {
        return radius;
    }
    
    /**
     * Sets the radius of the Cylinder
     * @param newRadius the value of the new radius
     */
    public void setRadius(int newRadius)
    {
        radius = newRadius;
    }
    
    /**
     * Gets the height of this Cylinder
     * @return the height of the Cylinder
     */
    public double getHeight()
    {
        return height;
    }
    
    /**
     * Sets the height of the Cylinder
     * @param newHeight the value of the new height
     */
    public void setHeight(int newHeight)
    {
        height = newHeight;
    }
    
     /**
     * Returns volume of cylinder.
     * @return theVolume the volume.
     */
    public double volume()
    {
       double theVolume;
       theVolume = ((Math.PI) * radius * radius * height);
       return theVolume;
    }
}