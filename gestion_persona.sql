DROP TABLE IF EXISTS personas;

CREATE TABLE personas (
  cedula VARCHAR(20) NOT NULL,
  nombre VARCHAR(100) NOT NULL,
  telefono VARCHAR(20),
  direccion VARCHAR(100) NOT NULL,
  estrato VARCHAR(100) NOT NULL, 
  eps VARCHAR(50) NOT NULL,
  fecha DATE NOT NULL,
  correo VARCHAR(100) NOT NULL,
  PRIMARY KEY (cedula)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
