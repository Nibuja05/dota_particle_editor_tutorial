---


---

<p>back to the <a href="../Tutorials.md">Tutorials</a>.</p>
<h1 id="sprite-trails">Sprite Trails</h1>
<p><a href="../Function%20Library.md#render-sprite-trail">Render sprite trail</a> is one of the hardest render methods to understand. Some interesting things about this totally awesome renderer are discussed here.</p>
<h2 id="static-sprite-trails">1. Static Sprite Trails</h2>
<p>What is the problem? Sometimes you may need to render a sprite trail for various reasons (e.g. trail end coloring, etc) but may also want the behavior that is more like that of a rope.</p>
<p>So I’m going to present a way that let’s you create a static sprite trail (no flickering) that be controlled by two CPs: One for the origin of the particle and one for the direction.</p>
<h3 id="step-1-creating-the-base">Step 1: Creating the base</h3>
<p>First we’re going to create a simple base particle effect, which serves as the basic foundation for all the following changes. So we need:</p>
<ul>
<li><code>Emit instantaneously</code> with a count of <code>1</code></li>
<li><code>Position within sphere random</code></li>
<li><code>Lifespan decay</code> with an endcap state of 1 (so we don’t need to change the lifetime for now)</li>
<li><code>Movement lock to control point</code></li>
<li><code>Render sprite trail</code> optional with any sprite trail you like (basic is enough)</li>
<li><code>Velocity random</code> with a min and max speed of <code>200</code> and any local coordinates for the direction you like<br>
You may also adjust the radius to get a better view of your particle</li>
</ul>
<h3 id="step-2-calculating-the-velocity">Step 2: Calculating the velocity</h3>
<p>Now we’re adding a lot of Pre Emission Operators for some calculations we need to make. To watch these CP changes in action it is advantageous to enable <code>Show Control Points</code> in the Particle Visualizer.<br>
First we need to add <code>Set CP orientation to point at second CP</code> to rotate our first CP in the direction of our second CP. You can choose any CPs for this, but in the following I’m refereing to the first CP as CP0 and the second one as CP1. If you choose these CPs, we can leave this operator in its default state.<br>
Secondly, we need to create the CP that will control our dynamic velocity. For that we’re using <code>Set single control point position</code> with CP2 as <code>control point number</code>. Now we can also set the distance this CP will be away from our origin thorugh changing the x value of <code>control point location</code>. For now let’s set the x value to <code>-400</code>. If you have the visualizer active you should see a new CP appearing and moving when you change the position of CP0 or CP1.<br>
Our next and last CP will be CP3. To calculate its proper position we need to calculate: <code>CP2 - CP0 = CP3</code>. Since we cannot do vector math directly we split it into 3 parts for the x,y and z value. Let’s create <code>Set control point component to scalar expression</code> three times.<br>
For all:</p>
<ul>
<li>set <code>expression</code> to <code>subtract</code></li>
<li>set <code>output control point</code> to <code>3</code></li>
<li>set <code>input1</code> to a <code>CP Component</code> with <code>CP2</code></li>
<li>set <code>input2</code> to a <code>CP Component</code> with <code>CP0</code></li>
</ul>
<p>Now we customize them for x,y and z:</p>
<ul>
<li>set the <code>output component</code> to either X, Y or Z</li>
<li>set the CP field to <code>.X</code> for <code>input1</code></li>
<li>set the CP field to <code>.X</code> for <code>input2</code><br>
If you move CP0 or CP1 now, CP3 should move accordingly</li>
</ul>
<h3 id="step-3-adding-the-velocity">Step 3: Adding the velocity</h3>
<p>Now all thats left to do is to add this calculated CP3 as velocity to our particle. For that we just need to add <code>Remap control point to velocity</code> and set its <code>input control point number</code> to 3.<br>
You should now see your particle trail moving along with your CP0 and CP1. You should also remove the <code>Velocity random</code> from earlier, since we don’t need it anymore.</p>
<h3 id="step-4-controlling-the-effect">Step 4: Controlling the effect</h3>
<p>You have a lot of control over the sprite trail right now. If you want to stretch it, you just need to change the number in our <code>Set single control point position</code> operator from earlier. I think <code>-4000</code> is quite a good number. If the number is positive you can inverse the direction the trail is facing. You can also control it with the <code>max length</code> property of <code>Render sprite trail</code>.<br>
Currently the sprite trail always rotates directly around its origin. But maybe you want the origin to be in the center or any other offset in the sprite trail. For that we can use the property <code>trail forward shift</code>. Just experiment with the value until you’re satisfied.</p>

