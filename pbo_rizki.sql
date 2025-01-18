-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 18, 2025 at 09:21 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pbo_rizki`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers_rizki`
--

CREATE TABLE `customers_rizki` (
  `cus_id` int(11) NOT NULL,
  `cus_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customers_rizki`
--

INSERT INTO `customers_rizki` (`cus_id`, `cus_name`) VALUES
(1, 'Ujang'),
(102, 'Ujang stephen');

-- --------------------------------------------------------

--
-- Table structure for table `electric_motorcycles_rizki`
--

CREATE TABLE `electric_motorcycles_rizki` (
  `id_product` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `battery` int(11) DEFAULT NULL,
  `mileage` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `electric_motorcycles_rizki`
--

INSERT INTO `electric_motorcycles_rizki` (`id_product`, `name`, `price`, `battery`, `mileage`) VALUES
(1, 'E-Motor Rizki Lite', 25000000, 1500, 120),
(2, 'E-Motor Rizki Pro', 35000000, 2000, 180);

-- --------------------------------------------------------

--
-- Table structure for table `motorcycles_rizki`
--

CREATE TABLE `motorcycles_rizki` (
  `id_product` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `cylinder` int(11) DEFAULT NULL,
  `tank_capacity` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `motorcycles_rizki`
--

INSERT INTO `motorcycles_rizki` (`id_product`, `name`, `price`, `cylinder`, `tank_capacity`) VALUES
(1, 'Motorcycle Rizki 150cc', 20000000, 150, 12),
(2, 'Motorcycle Rizki 250cc', 30000000, 250, 15);

-- --------------------------------------------------------

--
-- Table structure for table `orders_rizki`
--

CREATE TABLE `orders_rizki` (
  `id_order` int(11) NOT NULL,
  `customer` int(11) DEFAULT NULL,
  `product` varchar(255) DEFAULT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orders_rizki`
--

INSERT INTO `orders_rizki` (`id_order`, `customer`, `product`, `date`) VALUES
(1, 101, 'Helmet Rizki', '2025-01-14'),
(2, 102, 'E-Motor Rizki Lite', '2025-01-15'),
(102, 102, 'Motorcycle Rizki 150cc baru', '2025-03-05'),
(1001, 102, 'E-Motor Rizki Lite', '2025-03-02'),
(50515, 102, 'Sosis panjang lezat smoky', '2025-05-01');

-- --------------------------------------------------------

--
-- Table structure for table `product_rizki`
--

CREATE TABLE `product_rizki` (
  `id_product` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_rizki`
--

INSERT INTO `product_rizki` (`id_product`, `name`, `price`) VALUES
(1, 'Helmet Rizki', 500000),
(2, 'Motor Oil Rizki', 150000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customers_rizki`
--
ALTER TABLE `customers_rizki`
  ADD PRIMARY KEY (`cus_id`);

--
-- Indexes for table `electric_motorcycles_rizki`
--
ALTER TABLE `electric_motorcycles_rizki`
  ADD PRIMARY KEY (`id_product`);

--
-- Indexes for table `motorcycles_rizki`
--
ALTER TABLE `motorcycles_rizki`
  ADD PRIMARY KEY (`id_product`);

--
-- Indexes for table `orders_rizki`
--
ALTER TABLE `orders_rizki`
  ADD PRIMARY KEY (`id_order`);

--
-- Indexes for table `product_rizki`
--
ALTER TABLE `product_rizki`
  ADD PRIMARY KEY (`id_product`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
