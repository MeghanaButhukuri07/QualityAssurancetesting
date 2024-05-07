# physics.py

import math

# Pressure function to calculate pressure
def pressure(force, area):
    return force / area

# Force function to calculate force
def force(mass, acceleration):
    return mass * acceleration

# Speed function to calculate speed of object
def speed(distance, time):
    return distance / time

# Velocity function to calculate velocity of object
def velocity(displacement, time):
    return displacement / time

# Acceleration function to calculate acceleration
def acceleration(initial_velocity, final_velocity, time):
    return (final_velocity - initial_velocity) / time

# Momentum function to calculate momentum
def momentum(mass, velocity):
    return mass * velocity

# Work function to calculate work done
def work(force, distance):
    return force * distance

# Kinetic energy function
def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity**2

# Potential energy function
def potential_energy(mass, height, gravity=9.81):
    return mass * gravity * height

# Power function to calculate power
def power(work, time):
    return work / time

# Density function to calculate density
def density(mass, volume):
    return mass / volume

# Impulse function to calculate impulse
def impulse(force, time):
    return force * time

# Frequency function to calculate frequency from period
def frequency(period):
    return 1 / period

# Period function to calculate period from frequency
def period(frequency):
    return 1 / frequency

# Gravitational force function (Newton's Law of Universal Gravitation)
def gravitational_force(m1, m2, distance, G=6.67430e-11):
    return G * m1 * m2 / distance**2

# Heat energy function (Q = mcT)
def heat_energy(mass, specific_heat, delta_temp):
    return mass * specific_heat * delta_temp

# Angular velocity function
def angular_velocity(theta, time):
    return theta / time

# Torque function
def torque(force, lever_arm):
    return force * lever_arm

# Angular momentum function
def angular_momentum(moment_of_inertia, angular_velocity):
    return moment_of_inertia * angular_velocity

# Gravitational potential energy (for two masses)
def gravitational_potential_energy(m1, m2, distance, G=-1.67430e-11):
    return -G * m1 * m2 / distance

# Centripetal force function
def centripetal_force(mass, velocity, radius):
    return mass * velocity**2 / radius

# Centripetal acceleration function
def centripetal_acceleration(velocity, radius):
    return velocity**2 / radius

# Coulomb's Law function (electrostatic force)
def coulombs_law(k, q1, q2, distance):
    return k * q1 * q2 / distance**2

# Ohm's Law function (V = IR)
def ohms_law(current, resistance):
    return current * resistance

# Root mean square speed function (for ideal gases)
def rms_speed(temperature, molar_mass):
    return math.sqrt((3 * 8.314 * temperature) / (molar_mass * 0.001))

# Escape velocity function (for an object leaving a planet's surface)
def escape_velocity(gravity, radius):
    return math.sqrt(2 * gravity * radius)

# Doppler effect function (for frequency or wavelength)
def doppler_effect(initial_frequency, observer_speed, source_speed, speed_of_sound):
    return initial_frequency * ((speed_of_sound + observer_speed) / (speed_of_sound - source_speed))

# Index of refraction function (Snell's Law)
def index_of_refraction(angle_of_incidence, angle_of_refraction):
    return math.sin(angle_of_incidence) / math.sin(angle_of_refraction)

# Power in an electric circuit (P = IV)
def electric_power(current, voltage):
    return current * voltage

# Magnetic force function (Lorentz Force Law)
def magnetic_force(charge, velocity, magnetic_field):
    return charge * velocity * magnetic_field

# Photoelectric effect function (Einstein's Equation)
def photoelectric_effect(h, frequency, work_function):
    return h * frequency - work_function