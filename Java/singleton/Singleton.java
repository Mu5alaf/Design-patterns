/*
 * @Mu5alaf
 */

public class Singleton
{
    public static void Singleton(String[] args)
    {
        Abc obj1 = Abc.getInstance();
        Abc obj2 = Abc.getInstance();
        
        System.out.print(obj1);
        System.out.print(obj2);
    }
}

class Abc
{
    static Abc obj = new Abc();
    private Abc()
    {

    }
    public static Abc getInstance()
    {
        return obj;
    }
}