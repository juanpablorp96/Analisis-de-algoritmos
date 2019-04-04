import static org.junit.Assert.*;

import org.junit.Test;

public class SumadorCadenasTest {

	@Test
	public void testDeberiaDarCeroSiVacio() {
		String entrada = "";
		SumadorCadenas sumador = new SumadorCadenas();
		
		int resultado = sumador.sumarCadena(entrada);
		
		assertEquals(0, resultado);
	}
	
	@Test
	public void testDeberiaDarUnoSiVaUnSoloUno() {
		String entrada = "1";
		SumadorCadenas sumador = new SumadorCadenas();
		
		int resultado = sumador.sumarCadena(entrada);
		
		assertEquals(1, resultado);
	}
	
	@Test
	public void testDeberiaDar23SiVa15Coma8() {
		String entrada = "15, 8";
		SumadorCadenas sumador = new SumadorCadenas();
		
		int resultado = sumador.sumarCadena(entrada);
		
		assertEquals(23, resultado);
	}

}
