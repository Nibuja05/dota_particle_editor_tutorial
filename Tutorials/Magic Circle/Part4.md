back to the [Tutorials](../../Tutorials.md).

# Part 4: Living Pulse

Now we want to create a little extra to emphasize the magic circle effect. It is basically the same, but slighly bigger and less visible:

![](https://i.imgur.com/jh7YURJ.gif)

## The basics

This time we're actually not creating the effect from scratch. Since its basically the same as our parent particle, just open `magic_circle.vpcf` and use the *save as* function to save it as `magic_circle_pulse.vpcf`. Also be sure to remove all children.

Now go to `Render sprites` and change *alpha scale* to **0.3**. Sometimes it can be also quite useful to directly change values like alpha here.

## New radius

Even though it's basically the same effect, there's still a lot to change. First of all, we need to remove the `Radius scale` Operator. We're now going to recreate it a little different.

Let's add `Set Float` and change its value to `Particle Age (0-1)` and change the mode to `Curve`. Also set the value method to `Scale Initial Value`. Now, you should see the effect slowly scaling over time until it reaches 100%.

With the curve tool we can now try to recreate the previous radius scale effect. Try to match this curve:

![](https://i.imgur.com/WdtzXFf.png)

Right-Click on the second point to set its mode to `Free`. Then you can rotate it, so you can get a "curvy" line between point 1 and 2. With these changes, the result should look like the original with `Radius scale`.

Now we want it to be pulsating. Deactivate our `Set Float` we've just created for now and create a new one after that. For this one we set it to *Radius* again and choose `Scale Initial Value`. For the value we're going to use the `Noise` tool. A big subwindow should open with a lot of possible options. These values won't be explained right now, but try to recreate the following:

![](https://i.imgur.com/o8OdWmF.png)

With noise, we can get an effect that seems to be random, but is still adjustable to our liking. The radius of our particle should now pulse in an irregular pattern.

The last step is to combine these 2 actions. In order to do so, we need to make some adjustments. In both `Set Float` Operators, please change the method to `Set Value` and set one to put out `Scratch float 1` and the other to `Scratch float 2`. This way we save these values in seperate fields.

Now we add the `Set attribute to scalar expression` Operator and change its method to `Scale Initial Value`. This operator simply takes two values, calculates a new one from these inputs and writes in to the output. It is a very powerful tool, because it can calculate this for each individual particle. For our purpose we need it to `Multiply`. As inputs we choose `Per-Particle Float` for both and set them to `Scratch float 1` and `Scratch float 2`.

With this we have successfully combined our behaviours.

## Move on

Another effect is finished and the end is near. You can also add this effect to the parent now. In the last part, we're going to coordinate some things, so the effect functions as a whole and not just as a collection of some effects.

[<< Previous <<](./Part3.md) - [Introduction](./Introduction.md) - [Part 1](./Part1.md) - [Part 2](./Part2.md) - [Part 3](./Part3.md) - <b>[Part 4](#)</b> - [Part 5](./Part5.md) - [>> Next >>](./Part5.md)
