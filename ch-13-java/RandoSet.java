import java.util.Random;
import java.util.ArrayList;
import java.util.concurrent.Callable;

public class RandoSet {
  private String[] array;
  private Random random;
  
  public RandoSet(String[] array, int seed) {
    this.array = array;
    this.random = new Random(seed);
  }
  
  public ArrayList<String> randomSubset() throws Exception {
    ArrayList<String> subset = new ArrayList<String>();
    Callable<Boolean> include = () -> { return random.nextBoolean(); };
    for (String item : array) {
      if (include.call()) {
        subset.add(item);
      }
    }
    return subset;
  }
}
