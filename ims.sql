-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 01, 2019 at 02:11 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.1.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ims`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL,
  `customer_name` varchar(50) NOT NULL,
  `customer_phone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customer_id`, `customer_name`, `customer_phone`) VALUES
(1, 'Haymant', 123),
(293, 'bjbj', 2535),
(510, 'harman sandhu', 365367),
(514, 'iad', 12332),
(666, 'uadn', 123),
(777, 'njfan', 123),
(815, 'Hayadm', 123),
(967, 'ffdfd', 3435),
(978, 'bhalla', 55);

-- --------------------------------------------------------

--
-- Table structure for table `cust_trans`
--

CREATE TABLE `cust_trans` (
  `customer_id` int(11) NOT NULL,
  `customer_trans_id` int(11) NOT NULL,
  `data` varchar(10) NOT NULL,
  `amount` int(11) NOT NULL,
  `inv_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `purchase_bill`
--

CREATE TABLE `purchase_bill` (
  `purchase_id` int(11) NOT NULL,
  `balance` int(11) NOT NULL,
  `date` varchar(10) NOT NULL,
  `mode` int(11) NOT NULL,
  `amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `purchase_stock`
--

CREATE TABLE `purchase_stock` (
  `purchase_id` int(11) NOT NULL,
  `item_no` int(11) NOT NULL,
  `qty` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `sales_bill`
--

CREATE TABLE `sales_bill` (
  `inv_id` int(11) NOT NULL,
  `date` varchar(10) NOT NULL,
  `amount` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sales_bill`
--

INSERT INTO `sales_bill` (`inv_id`, `date`, `amount`, `customer_id`) VALUES
(1160, '2019-11-14', 660, 1),
(1361, '2019-11-21', 44, 293),
(1583, '2019-11-03', 132, 1),
(1839, '2019-11-02', 220, 514),
(2720, '2019-11-03', 517, 1),
(2866, '2019-11-22', 2, 510),
(2934, '2019-11-06', 264, 777),
(3435, '2019-11-22', 11, 967),
(5602, '2019-11-21', 220, 978),
(6804, '2019-11-21', 132, 815),
(6907, '2019-11-03', 132, 1),
(9474, '2019-11-03', 572, 1),
(9735, '2019-11-15', 264, 666);

-- --------------------------------------------------------

--
-- Table structure for table `sales_stocks`
--

CREATE TABLE `sales_stocks` (
  `inv_id` int(11) NOT NULL,
  `item_no` int(11) NOT NULL,
  `qty` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sales_stocks`
--

INSERT INTO `sales_stocks` (`inv_id`, `item_no`, `qty`) VALUES
(3542, 782, 1),
(1839, 782, 1),
(9474, 451, 1),
(9474, 782, 2),
(1583, 451, 1),
(6907, 451, 1),
(2720, 451, 2),
(2720, 583, 1),
(2934, 451, 2),
(1160, 297, 9),
(1160, 451, 2),
(9735, 451, 2),
(6804, 297, 3),
(1361, 297, 1),
(5602, 297, 5),
(2866, 254, 1),
(3435, 254, 5);

-- --------------------------------------------------------

--
-- Table structure for table `stocks`
--

CREATE TABLE `stocks` (
  `item_no` varchar(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `qty` int(11) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `stocks`
--

INSERT INTO `stocks` (`item_no`, `name`, `qty`, `price`) VALUES
('254', 'candy', 144, 2),
('297', 'face wash', 1, 40),
('451', 'Face Wash', 1, 120),
('583', 'Liquid Wash', 4, 230),
('656', 'face wash', 2, 40),
('691', 'Hand Wash', 2, 130),
('713', 'Lipstick', 5, 240),
('782', 'Body Wash', 9, 200),
('810', 'def', 5, 100),
('904', 'Liquid Cleaner', 5, 500);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `sr` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`sr`, `username`, `pass`) VALUES
(1, 'admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `wholesaler`
--

CREATE TABLE `wholesaler` (
  `whole_id` int(11) NOT NULL,
  `whole_name` varchar(50) NOT NULL,
  `whole_phone` int(11) NOT NULL,
  `whole_address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `whole_trans`
--

CREATE TABLE `whole_trans` (
  `whole_id` int(11) NOT NULL,
  `purchase_id` int(11) NOT NULL,
  `date` varchar(10) NOT NULL,
  `amount` int(11) NOT NULL,
  `whole_trans` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customer_id`);

--
-- Indexes for table `cust_trans`
--
ALTER TABLE `cust_trans`
  ADD PRIMARY KEY (`customer_trans_id`);

--
-- Indexes for table `purchase_bill`
--
ALTER TABLE `purchase_bill`
  ADD PRIMARY KEY (`purchase_id`);

--
-- Indexes for table `sales_bill`
--
ALTER TABLE `sales_bill`
  ADD PRIMARY KEY (`inv_id`);

--
-- Indexes for table `stocks`
--
ALTER TABLE `stocks`
  ADD PRIMARY KEY (`item_no`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`sr`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `wholesaler`
--
ALTER TABLE `wholesaler`
  ADD PRIMARY KEY (`whole_id`);

--
-- Indexes for table `whole_trans`
--
ALTER TABLE `whole_trans`
  ADD PRIMARY KEY (`whole_trans`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `sr` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
