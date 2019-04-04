
public class SumadorCadenas {
	public int sumarCadena(String cadena) {
		if ("".equals(cadena))
			return 0;
		else {
			String sumandos[] = cadena.split(",");
			if (sumandos.length == 1)
				return Integer.parseInt(sumandos[0]);
			return Integer.parseInt(sumandos[0]) + Integer.parseInt(sumandos[1]);
		}
	}

}
