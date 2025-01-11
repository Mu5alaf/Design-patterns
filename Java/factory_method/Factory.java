public class Factory {
    public static void Factory(String[] args)
    {
        final String candyType = "START_BURST";
        final CandyStore store = new CandyStore();
        store.sellCandy(candyType);
    }
}
class CandyStore{
    public void sellCandy(final String candyType){
        final Candy candy = switch (candyType) {
            case "GUM_DROP" -> new GumDrop();
            case "STAR_BURST" -> new StartBurst();
            default -> throw new IllegalArgumentException("Bad Candy Type");
        };
        System.out.printf("SOLD: A %s Which is %s units sweet",candy.name(), candy.sweetnees());    
    }
}

