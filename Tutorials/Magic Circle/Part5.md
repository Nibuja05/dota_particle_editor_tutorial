back to the [Tutorials](../../Tutorials.md).

# Part 5: The End

We're nearly done and only a handful of adjustments are left to do. So let's get to work and finish everything!

## Absolute timing

While using the normal `Alpha fade in/out simple` is quite easy to use and definatly a powerful tool, it has some big weaknesses: It is always proportianal to the life time. Often this is no problem, because the particles have a fixed life time. But in our case, this value can be set to anything we like. If you try to enter a high value like **20**, you'll see that the fading time takes forever and is not really what you want.

To fix this problem, we will set our life time to a fixed value instead and kill it another way. So first lets remove the following from our parent effect:

- `Lifetime random`
- `Remap control point to scalar` which adjusted the `Life Duration`
- `Alpha fade out simple`
- `Lifespan decay`

Also set the *end time* fo the `Radius Scale` to **0.6** and the fade time of `Alpha fade in simple` to **0.5**.

Now we need a new way to kill the particle effect: There is a `Pre Emission Operator` called `Stop effect after duration`. It's a powerful tool that can stop the effect and all its children after a certain time. Let's add it to our parent particle effect and set its duration to CP1-X. Now our effect is going to end after the desired time, but we still have fixed fading times.

Since we removed our old decay method, we also need a new one there. For this we're going to use `Lifespan endcap timed decay`. This decay method destroy the effect, when it is explicitly requested (like from `Stop effect after duration` or by killing it from *lua*) and after an additional duration we can specify under *decay time*. Set this value to **0.2**.

Now we only need a proper fade out when the particle is killed. For that we need `Lerp endcap scalar`. Leave its *output field* at `Radius` and set *value to lerp to* to **0**. Also set the *lerp time* to **0.4**. Now, if the particle dies it will change the radius to 0 over 0.4 seconds. Add this Operator a second time, this time for `Alpha` and set the *lerp time* to **0.2**.

Now we've successfully made the fade in and out effect absolute and independent of our duration. The next step is to the same for our children:

## Adjust the childs

Let's start with `magic_circle_pulse.vpcf`, since its a lot like our parent particle effect.

*Add everything you think might be needed now. If you think you're done, click to see the solution below.*

<details>
	<summary><b>Pulse Adjustments</b></summary>

Remove:
- `Lifetime random`
- `Remap control point to scalar` for the `Life Duration`
- `Lifespan decay`
- `Alpha fade out simple`

Copy:
- `Lifespan endcap timed decay`
- both `Lerp endcap scalar`

Adjust:
- the first `Set Float` (the one without noise)
- adjust the graph to be like this:

![](https://i.imgur.com/jwlYl0S.png)

</details>

Next is `magic_circle_ring.vpcf`. We haven't set the life duration here before, so we have a little less work to do.

- replace `Lifespan decay` with `Lifespan endcap timed decay`
- copy the alpha lerp from the parent here. Set the *lerp time* to **0.1**.

The last one is `magic_circle_sparks.vpcf`. Contrary to the other ones, we won't remove `Lifespan decay` here. We spawn new particles continiously, so if we would remove this decay operator here, they would never die and overload our system (so it will stop emitting after a short while).

However, we are not forced to only use a single decay operator, so we simply add `Lifespan endcap timed decay` on top of that. Also copy the alpha `Lerp endcap scalar` here too. Set the *lerp time* from both of them to **0.3**, so they will exist a little longer than the other effects.

**Note:** You wan't need `Stop effect after duration` in any child effect, since they are also affected from the parent one.

## Closing words

You have made it! You created a partice effect from scratch, that uses a variety of new methods and is anything else than easy to create. Even if this was a guided tutorial, you still created everything by yourself and thought of solutions alone.

I hope this guide was able to help you with your future particle creations. You have learned the general procedure to create a new more advanced effect and also a lot of tricks along the way.

If you got any suggestions for this guide, or have a request for another one, feel free to contact me any time.

[<< Previous <<](./Part4.md) - [Introduction](./Introduction.md) - [Part 1](./Part1.md) - [Part 2](./Part2.md) - [Part 3](./Part3.md) - [Part 4](./Part4.md) - <b>[Part 5](#)</b>
