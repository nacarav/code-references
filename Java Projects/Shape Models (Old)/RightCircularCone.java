/**
 * Models a Right circular cone
 * @author Nick Caravaggio
 */
public class RightCircularCone implements GeometricSolid
 
{
    private double radius;
    private double height;

    /**
     * Constructor for objects of class RightCircularCone
     * @param radius the radius of the RightCircularCone
     * @param height the height of this RightCircularCone
     */
    public RightCircularCone(double radius, double height)
    {
        this.radius = radius;
        this.height = height;
    }
    
    /**
     * Gets the radius of this RightCircularCone
     * @return the radius of the RightCircularCone
     */
    public double getRadius()
    {
        return radius;
    }
    
    /**
     * Sets the radius of the RightCircularCone
     * @param newRadius the value of the new radius
     */
    public void setRadius(double newRadius)
    {
        radius = newRadius;
    }
    
    /**
     * Gets the height of this RightCircularCone
     * @return the height of the RightCircularCone
     */
    public double getHeight()
    {
        return height;
    }
    
    /**
     * Sets the height of the RightCircularCone
     * @param newHeight the value of the new height
     */
    public void setHeight(double newHeight)
    {
        height = newHeight;
    }
    
     /**
     * Returns volume of Right Circular cone.
     * @return theVolume the volume.
     */
    public double volume()
    {
       double theVolume;
       theVolume = ((Math.PI) * radius * radius * (height / 3));
       return theVolume;
    }
   
}