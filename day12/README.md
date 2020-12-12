# Day 12

## Part 1

Similar to previous day's problem, there are a lot of details in this problems that need to be handled and kept track of. There are several states of the ship we need to track: its `x` position, `y` position, and the direction the ship is facing. This is again a good case of creating a `Ship` class to handle the information.

We begin again by breaking down the problem into small, testable chunks and then piece the chunks together at the end into a working solution. The chunks I broke the problem down into are as follows:

* Initialize the ship's initial state (start at `(0,0)` of the coordinate facing `EAST`)
* Move the ship's coordinates in a certain direction a certain amount
* Rotate the direction the ship is facing

We make several assumptions here; the biggest one is that the ship's rotation value is always a multiple of 90. In the real world, we probably should verify that this assumption is correct but because it's advent of code, we go with this assumption (the math would get really complicated otherwise).

As I began working on `Ship.__init__()`, I quickly realized that I'll be referencing the compass diretions a lot. Not wanting to hardcode `"N"`, `"W"`, `"S"`, `"E"`, I made an enum to express these ideas. I thought this would help my code be more readable and also help differentiate the idea of the direction the ship is facing and the character of the instruction.

I created a separate function that only concerned itself with moving the ship's location in some direction without worrying about the ship's direction and the instructions being passed from the input file. This makes the function testable; I can test moving the ship in every direction without worrying about the instruction code. This gives me confidence that when I start considering the ship's direction and other business logic, I already am able to manipulate the ship's coordinates correctly.

Lastly, I created another function to alter the way the ship is facing. Again, I made this function simple and detached from the rest of the ship's logic. Because this rotation logic is one of the trickiest parts of the problem, I wanted to make sure that I can test this function easily and independently.

After all the pieces are made and tested, we simply stitch them together with the requirements.

To help with testing, I overrode the `__str__` function and made some other helper functions.

## Part 2

The important part of this problem is that the waypoint is always _relative to_ the ship's position. This means somehow the waypoint needs to know where the ship is and keep track of its grid coordinate accordingly.

I decided to express the waypoint's coordinates as relative to the ship's coordinates. This inherently meant that somehow, the waypoint and the ship needed to know each other's information. I decided to create a new class that managed both the waypoint and the ship. The main reason for this approach was to keep the `Ship` class's initial implementation in Part 1 intact. If I can use the `ShipWaypointManager` class to supply the `Ship` with the `Waypoint`'s information, I don't have to edit any of `Ship` class's code and use it as is.
