-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 30, 2022 at 08:35 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blog_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(1000) NOT NULL,
  `phone_num` text NOT NULL,
  `message` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sno`, `name`, `email`, `phone_num`, `message`) VALUES
(1, 'first_post', 'first_post@gmail.com', '123456678910', 'first_msg'),
(2, 'SHAILENDRA UPADHYAY', 'shailendraupadhyayiitbhu@gmail.com', '09057507600', 'msg1'),
(3, 'Shailu', 'mail2shailendranow@gmail.com', '09057507600', 'test message for automatic mails.'),
(4, 'Shailu', 'mail2shailendranow@gmail.com', '09057507600', 'test message for automatic mails.'),
(5, 'Shailu', 'mail2shailendranow@gmail.com', '09057507600', 'test message for automatic mails.'),
(6, 'Shailu', 'mail2shailendranow@gmail.com', '09057507600', 'test11111111'),
(7, 'shailu', 'mail2shailendranow@gmail.com', '09057507600', 'test11111111111111111'),
(8, 'shailu', 'mail2shailendranow@gmail.com', '09057507600', 'msg1111111111111111111111111'),
(9, 'shailu', 'mail2shailendranow@gmail.com', '09057507600', 'test mail 111111111111111111111111111111'),
(10, 'shailu', 'shailu@gmail.com', '9935184729', 'Shailu\'s message'),
(11, 'SHAILENDRA UPADHYAY', 'coyocode@gmail.com', '09057507600', 'hi from coyo app.');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` varchar(1000) NOT NULL,
  `content` varchar(1000) NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp(),
  `slug` varchar(50) NOT NULL,
  `image_file` varchar(25) NOT NULL,
  `subtitle` varchar(100) NOT NULL,
  `author` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `content`, `date`, `slug`, `image_file`, `subtitle`, `author`) VALUES
(1, 'this is my first post title edited', 'this is content edited', '2022-12-29', 'first--post', 'post-bg.jpg', 'first post subtitle edited', 'first_author edited'),
(2, 'second post title', 'second post content', '2022-12-28', 'second-post', 'post-bg.jpg', 'second post subtitle', 'second author'),
(3, 'skills', 'A skill is the learned ability to act with determined results with good execution often within a given amount of time, energy, or both. Skills can often be divided into domain-general and domain-specific skills. For example, in the domain of work, some general skills would include time management, teamwork and leadership, self-motivation and others, whereas domain-specific skills would be used only for a certain job. Skill usually requires certain environmental stimuli and situations to assess the level of skill being shown and used.', '2022-12-28', 'skills', 'post-bg.jpg', 'skill development', 'Shailendra Upadhyay'),
(4, 'Cricket', 'Cricket is a bat-and-ball game played between two teams of eleven players on a field at the centre of which is a 22-yard (20-metre) pitch with a wicket at each end, each comprising two bails balanced on three stumps. The batting side scores runs by striking the ball bowled at one of the wickets with the bat and then running between the wickets, while the bowling and fielding side tries to prevent this (by preventing the ball from leaving the field, and getting the ball to either wicket) and dismiss each batter (so they are \"out\")', '2022-12-28', 'cricket', 'post-bg.jpg', 'cricket overview', 'Shaliu');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
