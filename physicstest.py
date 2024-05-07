import unittest
from physics import *

class TestPhysicsFunctions(unittest.TestCase):

    def test_pressure(self):
        # Test when force and area are both positive
        self.assertAlmostEqual(pressure(50, 10), 5.0)
        self.assertAlmostEqual(pressure(100, 25), 4.0)
        # Test when force is zero
        self.assertEqual(pressure(0, 10), 0)
        # Test when area is zero (should raise a ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            pressure(50, 0)
        # Test when both force and area are zero (should raise a ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            pressure(0, 0)

    def test_force(self):
        # Test when mass and acceleration are both positive
        self.assertAlmostEqual(force(5, 10), 50)
        self.assertAlmostEqual(force(2, 7), 14)
        # Test when mass is zero
        self.assertEqual(force(0, 10), 0)
        # Test when acceleration is zero
        self.assertEqual(force(5, 0), 0)

    def test_speed(self):
        # Test when distance and time are both positive
        self.assertAlmostEqual(speed(100, 10), 10)
        self.assertAlmostEqual(speed(50, 5), 10)
        # Test when distance is zero
        self.assertEqual(speed(0, 10), 0)
        # Test when time is zero (should raise a ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            speed(100, 0)

    def test_velocity(self):
        # Test when displacement and time are both positive
        self.assertAlmostEqual(velocity(20, 5), 4)
        self.assertAlmostEqual(velocity(100, 20), 5)
        # Test when displacement is zero
        self.assertEqual(velocity(0, 5), 0)
        # Test when time is zero (should raise a ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            velocity(20, 0)

    def test_acceleration(self):
        # Test when initial_velocity, final_velocity, and time are all positive
        self.assertAlmostEqual(acceleration(0, 10, 2), 5)
        self.assertAlmostEqual(acceleration(20, 30, 5), 2)
        # Test when initial_velocity is greater than final_velocity (negative acceleration)
        self.assertAlmostEqual(acceleration(30, 20, 5), -2)
        # Test when time is zero (should raise a ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            acceleration(20, 30, 0)

    def test_momentum(self):
        # Test when mass and velocity are both positive
        self.assertAlmostEqual(momentum(5, 10), 50)
        self.assertAlmostEqual(momentum(2, 7), 14)
        # Test when mass is zero
        self.assertEqual(momentum(0, 10), 0)
        # Test when velocity is zero
        self.assertEqual(momentum(5, 0), 0)

    def test_work(self):
        # Test when force and distance are both positive
        self.assertAlmostEqual(work(50, 10), 500)
        self.assertAlmostEqual(work(20, 5), 100)
        # Test when force is zero
        self.assertEqual(work(0, 10), 0)
        # Test when distance is zero
        self.assertEqual(work(50, 0), 0)

    def test_kinetic_energy(self):
        # Test when mass and velocity are both positive
        self.assertAlmostEqual(kinetic_energy(5, 10), 250)
        self.assertAlmostEqual(kinetic_energy(2, 7), 49)
        # Test when mass is zero
        self.assertEqual(kinetic_energy(0, 10), 0)
        # Test when velocity is zero
        self.assertEqual(kinetic_energy(5, 0), 0)

    def test_potential_energy(self):
        # Test when mass, height, and gravity are all positive
        self.assertAlmostEqual(potential_energy(5, 10), 490.5)
        self.assertAlmostEqual(potential_energy(2, 7), 137.34)
        # Test when mass is zero
        self.assertEqual(potential_energy(0, 10), 0)
        # Test when height is zero
        self.assertEqual(potential_energy(5, 0), 0)

    def test_power(self):
        # Test when work and time are both positive
        self.assertAlmostEqual(power(500, 10), 50)
        self.assertAlmostEqual(power(200, 5), 40)
        # Test when work is zero
        self.assertEqual(power(0, 10), 0)
        # Test when time is zero (should raise a ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            power(50, 0)

    def test_density(self):
        # Test when mass and volume are both positive
        self.assertAlmostEqual(density(10, 5), 2.0)
        self.assertAlmostEqual(density(20, 10), 2.0)
        # Test when mass is zero
        self.assertEqual(density(0, 5), 0)
        # Test when volume is zero (should raise a ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            density(10, 0)

    def test_impulse(self):
        # Test when force and time are both positive
        self.assertAlmostEqual(impulse(50, 10), 500)
        self.assertAlmostEqual(impulse(20, 5), 100)
        # Test when force is zero
        self.assertEqual(impulse(0, 10), 0)
        # Test when time is zero
        self.assertEqual(impulse(50, 0), 0)

    def test_frequency(self):
        # Test when period is positive
        self.assertAlmostEqual(frequency(2), 0.5)
        self.assertAlmostEqual(frequency(0.5), 2)
        # Test when period is zero (should raise a ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            frequency(0)

    def test_period(self):
        # Test when frequency is positive
        self.assertAlmostEqual(period(0.5), 2)
        self.assertAlmostEqual(period(2), 0.5)
        # Test when frequency is zero (should raise a ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            period(0)

    def test_gravitational_force(self):
        # Test when masses, distance, and gravitational constant are positive
        self.assertAlmostEqual(gravitational_force(5, 10, 3), 1.1122888888888888e-10)
        self.assertAlmostEqual(gravitational_force(2, 7, 5), 8.053599999999999e-11)
        # Test when mass1 or mass2 is zero
        self.assertEqual(gravitational_force(0, 10, 3), 0)
        self.assertEqual(gravitational_force(5, 0, 3), 0)
        # Test when distance is zero (should raise a ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            gravitational_force(5, 10, 0)

    def test_heat_energy(self):
        # Test when mass, specific heat, and delta temperature are all positive
        self.assertAlmostEqual(heat_energy(5, 10, 20), 1000)
        self.assertAlmostEqual(heat_energy(2, 7, 10), 140)
        # Test when mass is zero
        self.assertEqual(heat_energy(0, 10, 20), 0)
        # Test when specific heat is zero
        self.assertEqual(heat_energy(5, 0, 20), 0)
        # Test when delta temperature is zero
        self.assertEqual(heat_energy(5, 10, 0), 0)

    def test_angular_velocity(self):
        # Test when theta and time are both positive
        self.assertAlmostEqual(angular_velocity(100, 10), 10)
        self.assertAlmostEqual(angular_velocity(50, 5), 10)
        # Test when theta is zero
        self.assertEqual(angular_velocity(0, 10), 0)
        # Test when time is zero (should raise a ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            angular_velocity(100, 0)

    def test_torque(self):
        # Test when force and lever arm are both positive
        self.assertAlmostEqual(torque(50, 10), 500)
        self.assertAlmostEqual(torque(20, 5), 100)
        # Test when force is zero
        self.assertEqual(torque(0, 10), 0)
        # Test when lever arm is zero
        self.assertEqual(torque(50, 0), 0)

    def test_angular_momentum(self):
        # Test when moment_of_inertia and angular_velocity are both positive
        self.assertAlmostEqual(angular_momentum(5, 10), 50)
        self.assertAlmostEqual(angular_momentum(2, 7), 14)
        # Test when moment_of_inertia is zero
        self.assertEqual(angular_momentum(0, 10), 0)
        # Test when angular_velocity is zero
        self.assertEqual(angular_momentum(5, 0), 0)

    def test_gravitational_potential_energy(self):
        # Test when masses, distance, and gravitational constant are all positive
        self.assertAlmostEqual(gravitational_potential_energy(5, 10, 3), -3.33715e-10)
        self.assertAlmostEqual(gravitational_potential_energy(2, 7, 5), -3.00756e-11)
        # Test when mass1 or mass2 is zero
        self.assertEqual(gravitational_potential_energy(0, 10, 3), 0)
        self.assertEqual(gravitational_potential_energy(5, 0, 3), 0)
        # Test when distance is zero (should raise a ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            gravitational_potential_energy(5, 10, 0)

    def test_centripetal_force(self):
        # Test when mass, velocity, and radius are all positive
        self.assertAlmostEqual(centripetal_force(5, 10, 3), 166.66666666666666)
        self.assertAlmostEqual(centripetal_force(2, 7, 5), 19.6)
        # Test when mass is zero
        self.assertEqual(centripetal_force(0, 10, 3), 0)
        # Test when velocity is zero
        self.assertEqual(centripetal_force(5, 0, 3), 0)
        # Test when radius is zero (should raise a ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            centripetal_force(5, 10, 0)

    def test_centripetal_acceleration(self):
        # Test when velocity and radius are both positive
        self.assertAlmostEqual(centripetal_acceleration(9, 3), 27)
        self.assertAlmostEqual(centripetal_acceleration(7, 5), 9.8)
        # Test when velocity is zero
        self.assertEqual(centripetal_acceleration(0, 3), 0)
        # Test when radius is zero (should raise a ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            centripetal_acceleration(10, 0)

    def test_coulombs_law(self):
        # Test when k, q1, q2, and distance are all positive
        self.assertAlmostEqual(coulombs_law(9e9, 1e-6, 2e-6, 1), 18)
        self.assertAlmostEqual(coulombs_law(9e9, -3e-6, 5e-6, 2), -337.5)
        # Test when k is zero
        self.assertEqual(coulombs_law(0, 1e-6, 2e-6, 1), 0)
        # Test when q1 or q2 is zero
        self.assertEqual(coulombs_law(9e9, 0, 2e-6, 1), 0)
        self.assertEqual(coulombs_law(9e9, 1e-6, 0, 1), 0)
        # Test when distance is zero (should raise a ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            coulombs_law(9e9, 1e-6, 2e-6, 0)

    def test_ohms_law(self):
        # Test when current and resistance are both positive
        self.assertAlmostEqual(ohms_law(2, 3), 6)
        self.assertAlmostEqual(ohms_law(1, 5), 5)
        # Test when current is zero
        self.assertEqual(ohms_law(0, 3), 0)
        # Test when resistance is zero
        self.assertEqual(ohms_law(2, 0), 0)

    def test_rms_speed(self):
        # Test when temperature and molar_mass are both positive
        self.assertAlmostEqual(rms_speed(300, 28.97), 516.4647275762623)
        self.assertAlmostEqual(rms_speed(500, 20), 675.2665363748444)
        # Test when temperature is zero
        self.assertEqual(rms_speed(0, 28.97), 0)
        # Test when molar_mass is zero (should raise a ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            rms_speed(300, 0)

    def test_escape_velocity(self):
        # Test when gravity and radius are both positive
        self.assertAlmostEqual(escape_velocity(9.81, 6371000), 11178.042851721911)
        self.assertAlmostEqual(escape_velocity(3.7, 3389500), 5021.019335255979)
        # Test when gravity is zero
        self.assertEqual(escape_velocity(0, 6371000), 0)
        # Test when radius is zero (should raise a ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            escape_velocity(9.81, 0)

    def test_doppler_effect(self):
        # Test when initial_frequency, observer_speed, source_speed, and speed_of_sound are all positive
        self.assertAlmostEqual(doppler_effect(1000, 10, 5, 343), 1043.2011677422833)
        self.assertAlmostEqual(doppler_effect(500, 20, 10, 343), 517.2610837438424)
        # Test when initial_frequency is zero
        self.assertEqual(doppler_effect(0, 10, 5, 343), 0)
        # Test when speed_of_sound is zero (should raise a ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            doppler_effect(1000, 10, 5, 0)

    def test_index_of_refraction(self):
        # Test when angle_of_incidence and angle_of_refraction are both positive
        self.assertAlmostEqual(index_of_refraction(math.radians(30), math.radians(20)), 1.5261919331696952)
        self.assertAlmostEqual(index_of_refraction(math.radians(45), math.radians(30)), 1.4142135623730951)
        # Test when angle_of_incidence is zero
        self.assertEqual(index_of_refraction(0, math.radians(20)), 0)
        # Test when angle_of_refraction is zero (should raise a ZeroDivisionError)
        with self.assertRaises(ZeroDivisionError):
            index_of_refraction(math.radians(30), 0)

    def test_electric_power(self):
        # Test when current and voltage are both positive
        self.assertAlmostEqual(electric_power(2, 3), 6)
        self.assertAlmostEqual(electric_power(1, 5), 5)
        # Test when current is zero
        self.assertEqual(electric_power(0, 3), 0)
        # Test when voltage is zero
        self.assertEqual(electric_power(2, 0), 0)

    def test_magnetic_force(self):
        # Test when charge, velocity, and magnetic_field are all positive
        self.assertAlmostEqual(magnetic_force(2, 3, 4), 24)
        self.assertAlmostEqual(magnetic_force(1, 5, 6), 30)
        # Test when charge is zero
        self.assertEqual(magnetic_force(0, 3, 4), 0)
        # Test when velocity is zero
        self.assertEqual(magnetic_force(2, 0, 4), 0)
        # Test when magnetic_field is zero
        self.assertEqual(magnetic_force(2, 3, 0), 0)

    def test_photoelectric_effect(self):
        # Test when h, frequency, and work_function are all positive
        self.assertAlmostEqual(photoelectric_effect(6.63e-34, 5e14, 3), 3.315e-18)
        self.assertAlmostEqual(photoelectric_effect(6.63e-34, 4e14, 2), 2.652e-18)
        # Test when h is zero
        self.assertEqual(photoelectric_effect(0, 5e14, 3), -3)
        # Test when frequency is zero
        self.assertEqual(photoelectric_effect(6.63e-34, 0, 3), -3)
        # Test when work_function is zero
        self.assertEqual(photoelectric_effect(6.63e-34, 5e14, 0), 3.315e-18)

if __name__ == '__main__':
    unittest.main()