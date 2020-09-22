back to the [Tutorials](../../Tutorials.md).

# Part 3: Outer Ring

In this part we're going to create an outer ring, that is rotating counterclockwise:

![](https://i.imgur.com/r22JsPe.gif)

## The basics

As you might have already guessed, we are creating the effect from scratch and need to start from a blank effect. Save it in the same folder as `magic_circle_ring.vpcf`.

As a starting point we want to create this effect:

![](https://i.imgur.com/u3ZGxfb.png)

Try to recreate that effect. That is not that easy, so in case you might need help, but don't want to see the solution, there are also some tips for you.

*Add everything you think might be needed now. If you think you're done, click to see the solution below.*

<details>
	<summary><i>Tip 1</i></summary>

 - a "Rope" might something that is close to what we need.

</details>

<details>
	<summary><i>Tip 2</i></summary>

 - the effect is emitted as a ring, we should look for something that does that.

</details>

<details>
	<summary><i>Tip 3</i></summary>

 - all particles seem to be "evenly spread" across the ring.

</details>

<details>
	<summary><b>Solution</b></summary>

 - use `Emit instantaneously` as Emitter
 - use `Position along ring` as positional Initialzer and set its initial radius to a bigger value, like **"200**
 - add a `Lifespan decay`
 - use `Render rope` as Renderer

`Render rope` takes a texture and tries to spread it evenly over all particles, so there are no seperate particles and instead one beam/rope. Use `/base_rope.vtex` as a texture. Also enable the option `Closed loop` to connect the first and last particle.

Don't forget to check `even distribution` in `Postion along ring` or else everything will be messy.

</details>

Next we add the usual, like a fade in effect and a color. Also we should increase the radius.

*Add everything you think might be needed now. If you think you're done, click to see the solution below.*

<details>
	<summary><b>Basic Functionality</b></summary>

- add `Color random` and choose two times the same color (matching your previously used colors) or change the color in the `Base Properties`
- add `Alpha fade in simple`
- add `Radius random` and choose two times the same value or change it in the `Base Properties`, set it to **25**

We won't need `Alpha fade out simple` for now, since we want to use another method later on.

Also set the operator end cap state of `Lifespan decay` to 1. This way the particles will never die, even if they exceed their lifespan. This is useful for testing and will be explained later on in this guide.

</details>

## Further shaping

Now it's time to set the shape of our ring. Until now we only have a basic ring, that is far away from the preview at the beginning. To achieve this effect, we will use a new feature called "curves".

Add a new Initializer called `Init Float`. This will simply set a particle property like the radius for each particle. First we want to set its value method to `Scale Initial Value`. This way, we can change the radius, while also keeping our intial value (of **25**).

We're going to use the `#` button again. Choose `Per-Particle Number Percent of Total Count (0-1)`. As the (long!) name impliesm, this value is different for each particle and returns a percentage value of its index. If you use the preview *Visualize* function (button at the top) and check `Show Particle Indices`, you can see, that the higher the particle index is, the greater the radius.

Close the *Visualizer* and change the mode from `Direct Value Copy` to `Curve`. With this function we can set a graph that maps our input values to output values. We can also define the value ranges we want to cover. For now let's set the maximum of `Output Range` to **2**.

Now let's add another point to the graph. To do so hover over a position, hold *Shift* and click to confirm. It's not the most intuitive function, but you'll get it done. Now move this new point to **(0.50, 2.00)** and the last point to **(1.00, 0.00)**. You should now see a shape that pretty close to what we're aiming for. You can adjust these points until you're happy with the result:

![](https://i.imgur.com/l9OweBz.png)

Now we add a second `Init Float` and want to achive something similiar for the `alpha` value.

*Add everything you think might be needed now. If you think you're done, click to see the solution below.*

<details>
	<summary><b>Alpha Curve</b></summary>

- set the value again to `Per-Particle Number Percent of Total Count (0-1)` and its mode to `Curve`. Leave all ranges at default.
- set the output field to `alpha`
- leave the value method at `Set Value`

It's also a good idea to adjust the curve a little further like here: 

![](https://i.imgur.com/l3X6u8y.png)

</details>

## Finishing touch

At the end we only have some little things to do. First let's not forget to set the max particle count to **100**. Also we should add `Normal lock to control point` like before, so the particles will follow the start CP.

We should also not forget to adjust the radius dynamically to CP2. This is done the same way as in the previous effect, we just need to set it for the initial radius value in `Position along ring` here.

Because we want the effect to be clearly visible "over" the main circle effect, we can also physically increase its height. To do so we add `Position modify offset random` and set the *Z*-coordinate of min and max to **15**.

Now, just some changes in the renderer are left:

- change the *orientation type* to `World-Z Align`, so the effect is following the ground and not the camera anymore (to match the magic circle).
- increase its *overbright factor* a little (something like **1.5**)
- change its texture to  `beam_plasma_08.vtex`
- under `Texture Coordinates`, set *texture V World Size* to **600**
- change *texture V Scroll Rate* to **-100** (or something higher)

The last step that's left to do is adding `Movement rotate particle around axis`. Choose a positive rotation rate (>50) and adjust it to your liking.

## Move on

The second child is done and only one left to go. When you wish, you could add this effect to the parent as well. You should visit this effect any time to make some adjustments in the graphs or other numbers, whenever you think somethings not quite right.

The next effect is a pulsating magic circle, so go check it out!

[<< Previous <<](./Part2.md) - [Introduction](./Introduction.md) - [Part 1](./Part1.md) - [Part 2](./Part2.md) - [Part 3](#) - [Part 4](./Part4.md) - [Part 5](./Part5.md) - [>> Next >>](./Part4.md)
