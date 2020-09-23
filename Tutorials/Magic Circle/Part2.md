back to the [Tutorials](../../Tutorials.md).

# Part 2: Sparkly Addition

In this part we're going to create sparks that emerge from the ground and circle in the same direction as our main circle particle. The final result should look like this:

![](https://i.imgur.com/Rkp1tXO.gif)

## The basics

As always we need to start with a fresh new particle. So open the Editor and press *Ctrl + N* to create a new particle effect and save it in the same directory as the circle as `magic_circle_sparks.vpcf`. It is common practice to keep the parent name and add the new addition, in this case *_sparks* at the end. This will ensure to make the hierachy also visible with the particle naming.

So to start, lets do some basic sprites that continiously spawn on the ground:

![](https://i.imgur.com/5MdkvaM.gif)

*Add everything you think might be needed now. When you think you're done, click to see the solution below.*

<details>
	<summary><b>Basic Functionality</b></summary>

- add an emitter: `Emit continously`.  Leave it at default properties for now.
- add a renderer: `Render sprites`. Leave it at default properties for now.
- add decay: `Lifespan decay`.
- spawn it: `Emit withing sphere random`. Leave `distance min` at **0** and set `distance max` to a higher value of your liking. In `distance bias` set the *Z*-coordinate to **0**, so the particles will all spawn at the same height.

</details>

Now that we have the bare minimum we can think of improving the effect. If you think of the circle effect, you can already imagine that we want some kind of fades for a smoother creation and end of the particles.

*Add everything you think might be needed now. When you think you're done, click to see the solution below.*

<details>
	<summary><b>Start/End</b></summary>

Let's add some fades first:
- `Alpha fade out simple` with default properties.
- `Alpha fade in simple` with a fade in time of **0.1** so it start smooth, but still more forceful.

Next we address the radius. For more variety we also should add:
- `Radius random` with something like **10-25**.

For fading it we use:
- `Radius scale` with an end time of **0.1** (matching the alpha fade). The scale should go from **0** to **2**.
- another `Radius scale` with a start time of **0.1** and an end time of **1**. It goes from **2** to **1**. Also we increase the scale bias to **0.8**.

Now the particles should start nearly instant, but still a bit smoother and slowly fade away after that.

</details>

## Visuals

Let's add some color next. We could just change it in the `Base Properties`, but for more variety we should use the `Color random` Initializer. Pick two shades of a dark purple, that you think might be a good match to your coloring of the main circle effect (or any other color, if you didn't made the main effect purple).

Also, let's add a `Color fade random` to the effect. Choose two brighter colors than you've used in the Initializer. Also set the fade end time to **0.6**, so the effect will fade there sooner.

Still until now, our effect doesn't look quite right. One reason for this is, that we still use the most basic sprite texture there is. While it may be enough for some cases, we want something more interesting.

So first we're going to change the sprite to `particle_glow_05.vtex`. You should be able to find it with the search function. With this change the effect should suddenly look a lot darker. This is because of the great "black" outline of this sprite texture. It should look like this: 

![](https://i.imgur.com/68ZtYKG.png)

To change this open `Color and alpha adjustments` in `Render Sprites`. Now check `use additive blending`. This Renderer now uses another coloring method and therefore all black is treated as the key for transperency. Now it should look really bright and nearly transparent:

![](https://i.imgur.com/MUfrmtA.png)

To address this new issue, we just need to increase the `overbright factor` in the same category. Slowly increase the value to see it's effects. The higher the value the more "saturated" the colors become. Increase it to **10**.

*Note: Whenever you feel like your effect is barely visible ingame, try adjusting this value.*

The result should now look like this:

![](https://i.imgur.com/hixB3aJ.png)

## Movement

Now that we have a nice static effect, we should add some movement as well. Try to add a "rising" effect and make the particles spin around the center.

*Add everything you think might be needed now. When you think you're done, click to see the solution below.*

<details>
	<summary><b>Basic Movements</b></summary>

You should have remembered, that for every particle movement `Movement basic` is needed. So let's add this Operator. To achieve a "rising" effect, we can simply enter a positive value for the *Z*-coordinate of `gravity`. Choose a value that isn't too high, something between **50-150**.

For the spinning, we can simply use `Movement rotate particle around axis`. We only need to change the rotation rate. Enter the same value as you've entered as rotation speed for the circle, so it matches it's rotation.

</details>

Now that we have the basic movement done, we still have some options to make the effect look more "alive". A great way to do so are `Force Generator`. They can add all kinds of interesting velocities to particles. So here a short break for a short velocity explanation:

### ~ Velocities ~

Each particle can have a velocity, which describes a speed the particle is moving in a certain direction. Opposing velocities can cancel each other or can add each other of they are facing in the same direction. Since a particle tries to maintain it's velocity all the time, they are nearly always applied as `Initializer`.

Some effects like `Movement rotate particle around axis` don't effect the velocity at all and just change the particles location additionally. Also note that all *speed* attributes of positional Initializers like in `Position within sphere random` are velocities as well.

On top of this, velocities can be over time after their inital values. For this, often `Force Generator` are used.

### ~ Velocities End ~

For this effect we're going to add `Noise force`, which applies random forces to our particles. We can leave every property at its default value and just change `noise amplitude`. Change all of its coordinates to **200**.

Now all that's left to do is to add `Movement lock to control point`. This will make all particles meintain their relative position to a certain CP. We don't need to change any properties here, so it will follow all changes of our start CP (0). This is also additional movement and no applied velocity.

## Scaling

We're nearly done with this child effect, but one this is still missing. Since we made our parent circle particle scaling by radius, we need to achieve this here too.

Go to our `Position within sphere random` Initializer and check its distance max value. Currently it is set to a fixed number. You might have noticed a little `#` button on its right side. Whenever you see this button, it means that instead of a fixed value, all kinds of other dynamic values can be used as well. Click on it and choose `CP component`. Now we can choose a CP and select *X, Y* or *Z* coordinate. Like the CP2-X we used there, we're going to do the same here. You can now adjust the radius where the sparks are emitted with CP2.

If you choose a low value or something really big, you might notice that the particle count is either to big or to low. To fix this we also need to make our emission speed dynamic. So choose `CP component` for emission rate in `Emit continuously` as well with CP2-X. Before we had a fixed **100**, which was quite optimal for radius for about **400**. To match this, we can use further manipulate this value. Below the former `#` Button is now a `=`, which means `Direct Value Copy`. Since we want about a fourth, we choose `Multiply` and set the value to **0.25**.

Now we've successfully setup our particle effect. There's only one thing left to do for now: Adjusting the max particle count. This is quite an important step, since it can impact your particles performance. Enter the highest radius you expect as *X*-coordinate for CP2 and check the active particle number at the top of your preview window. Use this as a reference and enter it as max particle number in your `Base Properties`.

## Move on

We finished our first child particle effect, so if you want you can also add it to it's parent now. Next we're going to make the next child, which is a spinning outer ring.

[<< Previous <<](./Part1.md) - [Introduction](./Introduction.md) - [Part 1](./Part1.md) - <b>[Part 2](#)</b> - [Part 3](./Part3.md) - [Part 4](./Part4.md) - [Part 5](./Part5.md) - [>> Next >>](./Part3.md)
