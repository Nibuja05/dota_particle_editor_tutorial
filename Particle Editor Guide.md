---


---

<p>back to the <a href="./README.md">Overview</a>.</p>
<h1 id="particle-editor-guide">Particle Editor Guide</h1>
<p>Welcome to the <strong>Particle Editor Guide</strong>.<br>
This guide will help you to get into touch with the editor and explain the basic functionality of particle effects. No matter if you’re a complete beginner or had already some contact with the editor, here’s the best place to start!</p>
<h2 id="content">Content</h2>
<ul>
<li><a href="#the-tool">The Tool</a>
<ul>
<li><a href="#menu">Menu</a></li>
<li><a href="#preview">Preview</a></li>
<li><a href="#functions">Functions</a></li>
<li><a href="#properties">Properties</a></li>
<li><a href="#controls">Controls</a></li>
<li><a href="#current-assets">Current Assets</a></li>
</ul>
</li>
<li><a href="#functions-1">Functions</a>
<ul>
<li><a href="#base-properties">Base Properties</a></li>
<li><a href="#emitter">Emitter</a></li>
<li><a href="#initializer">Initializer</a></li>
<li><a href="#operator">Operator</a></li>
<li><a href="#force-generator">Force Generator</a></li>
<li><a href="#constraint">Constraint</a></li>
<li><a href="#renderer">Renderer</a></li>
<li><a href="#pre-emission-operator">Pre Emission Operator</a></li>
</ul>
</li>
<li><a href="#what-now">What’s Next</a></li>
</ul>
<h2 id="the-tool">The Tool</h2>
<p>(<a href="https://developer.valvesoftware.com/wiki/Dota_2_Workshop_Tools/Particles/Particle_Editor">Valves official documentation of the Tool</a>)</p>
<p>There are two ways to open the Particle Editor: The first is to click on the flame symbol on the top left of the main asset browser window to open a blank new window. The second way is to directly open an existing particle effect by double clicking it in the asset browser.</p>
<p>Now open an existing particle effect as an example:</p>
<p>Note: If you can’t open a particle, and receive an error message with <code>No corresponding content file</code>, you cannot edit this particle effect, since valve only made the compiled version public.</p>
<h3 id="menu">Menu</h3>
<p>In the top left you have standard menu actions with File, Edit, View and Help. There’s nothing special about it and just some default operations like save, open etc.<br>
Important note here: In order to modify valves particles you need to save it in your current addon.</p>
<h3 id="preview">Preview</h3>
<p>The biggest part of your window should be filled with a preview part in the middle. There you can already see how the effect will eventually look like in the game. You can move freely with WASD, the right mouse button and the mouse wheel to see the effect from any side and distance. In the top left are two lines of text that display statistics of the number of particles.<br>
The icons in the top bar mainly handle the playback of the effect in the preview window. Here you can stop the simulation, restart it, etc.<br>
<img src="https://i.imgur.com/ktpuMb6.png" alt=""><br>
To the right there are two more buttons that can be used to reset the camera, e.g. if you have navigated the camera unfavorably.<br>
<img src="https://i.imgur.com/jMP5TY3.png" alt="alt text"><br>
The last button in the row is the most important one: Visualize allows you to graphically display various, otherwise invisible, attributes. It opens a small extra window where you can choose what you want to display.<br>
<img src="https://i.imgur.com/Mj7G1HC.png" alt="alt text"><br>
Most important is the first item <code>Visualize Attributes</code> which allows you to display specific attributes like radius, alpha etc. Also, <code>Show Control Points</code> which shows all currently active control points. If there is too much information, disable <code>Include Child Systems</code> to ignore the child effect data.</p>
<h3 id="functions">Functions</h3>
<p>The functions are the heart of every particle effect. Here you can define all properties and behaviors that make the effect what it is. In the upper part, there are also 4 small buttons that make navigation much easier.</p>
<p><img src="https://i.imgur.com/XppFQIR.png" alt="alt text"></p>
<p>If you have more than one effect open at the same time in the particle editor, you can jump to the last displayed effect with the left arrow. Likewise, the arrow to the right leads to the next effect. The button to the right is either grayed out and shows a P or a number. If the current effect is added to another effect as a child you can use it to display a list of these effects and jump to them. Vice versa the button next to it with a number or a capital C. This shows subordinate effects in a tree structure. If these two buttons are not clickable, it means that there are no effects available at the moment.<br>
More about the functions in detail here: <a href="#Functions-1">Functions</a>.</p>
<h3 id="properties">Properties</h3>
<p>The detailed data for the currently selected function is displayed here. If you want to make changes to one of the functions, this is the right place to do so.<br>
<img src="https://i.imgur.com/VLjTtIz.png" alt=""></p>
<h3 id="controls">Controls</h3>
<p>The control part is divided into two parts: the control points and preview. Control points are 3-dimensional vectors that form the interface between the particle effect and the code. They will allow you to place your particle effect exactly where you want them and let you control all kinds of behavior.<br>
<img src="https://i.imgur.com/1OU3mSS.png" alt="alt text"><br>
By clicking on the colored icon to the right of the arrow, you can directly influence these points, for example by moving or rotating them. Alternatively you can also enter your desired values in the fields next to it. On the far right you will find a small lock symbol. If it is closed, the entered values are saved, so that the next time you open this effect in the Particle Editor, the values are immediately restored to the saved values. With the preview part below, other assets like models can be loaded directly into the current effect. This is only a test tool and has no influence on the final result displayed in the game. Nevertheless, it is essential for quick testing of different effects.</p>
<h3 id="current-assets">Current Assets</h3>
<p>This part is like a small Asset Browser and can be used to reopen (focus) currently opened particle effects without leaving the particle editor. Most of the time you can/should minimize this to have more space for your preview and other windows.<br>
<img src="https://i.imgur.com/OgFzSDw.png" alt=""></p>
<h2 id="functions-1">Functions</h2>
<p>Now that you have learned the general handling of the tool, we can start to take a closer look at the functions that make every effect work. Functions are divided into different groups, that will be explained here. You can find a complete list of all functions with their usage here: <a href="./Function%20Library.md">Functions Library</a><br>
To add a function to one of these groups, just click the plus icon and choose an element from the list. You can also select multiple functions with <strong>ctrl</strong> or <strong>shift</strong> and copy, cut and paste with knows shortcuts (<em>ctrl + c, ctrl + x, ctrl + v</em>). These actions work accross multiple particle effects.</p>
<h3 id="base-properties">Base Properties</h3>
<p>The base properties hold every information about the effect, including all other groups. In addition, both initial and other important values can be found here. Some initial values that can be set here are explained below. These are attributes that are tied to every single particle in your effect and independant from each other</p>
<ul>
<li><code>color</code> - the color the particle is tinted with.</li>
<li><code>radius</code> - determines the size of this particle.</li>
<li><code>lifetime</code> -  this is the time in seconds, your particle will be alive, means it will be destroyed after this time.</li>
<li>others</li>
</ul>
<p>One of the most important fields here is <code>max particles</code> which is a hard cap to the number of particles maximal allowed for this effect (excluding child effects).</p>
<h3 id="emitter">Emitter</h3>
<p>Emitters are functions that can generate particles. They can therefore be found in almost every effect. Normally it is sufficient to use one kind of emitter. The most commonly used emitters among them are:</p>
<ul>
<li><code>Emit continuously</code> - emits particles in a set interval. <code>emission rate</code> is the count of particles emitted per second, <code>emission duration</code> is the duration in which particles are emitted and <code>emission start time</code> is a delay to the start of the emission in seconds. (<a href="./Function%20Library.md#emit-continuously">Library</a>)</li>
<li><code>Emit instantaneously</code> - emits <code>num to emit</code> particles directly at the start of the effect all at once. The emission can be delayed with <code>emission start time</code>. (<a href="./Function%20Library.md#emit-instantaniously">Library</a>)</li>
</ul>
<h3 id="initializer">Initializer</h3>
<p>Initializers are normally executed only once, when a particle is created. With their help particles get their initial values. An effect hardly ever gets along without initializers, especially since they play one of the most important roles in the operators: the placement of the particles.<br>
Often Initializers are used to set some randomized initial values:</p>
<ul>
<li><code>Lifetime random</code> - sets the lifetime of the spawned particle to a random value between <code>lifetime min</code> and <code>lifetime max</code>. (<a href="./Function%20Library.md#lifetime-random">Library</a>)</li>
<li><code>Radius random</code> - sets the radius of the spawned particle to a random value between <code>radius min</code> and <code>radius max</code>. (<a href="./Function%20Library.md#radius-random">Library</a>)</li>
<li><code>Rotation random</code> - randomizes the initial rotation of the particle between <code>yaw offset min</code> and <code>yaw offset max</code> plus <code>yaw initial</code> on top of that. Mostly <code>Roll</code> is the important field important for basic sprites. <code>randomly flip direction</code> can be checked to treat the min and max value, as if they were negated. (<a href="./Function%20Library.md#rotation-random">Library</a>)</li>
<li><code>Color Random</code> - sets the inital color to a random vector between <code>color 1</code> and <code>color 2</code>. Ignore all other fields for now, they are rarely used. (<a href="./Function%20Library.md#color-random">Library</a>)</li>
</ul>
<p>Besides these random value Initializers, the positional Initializers are the most important one. They determine where a particle is going to spawn. Also they have a lot of fields for adjustments, the basics will be explained below:</p>
<ul>
<li>
<p><code>Position within sphere random</code> - most used positional Initializer. Places new particles at a random position within a given radius around the center control point, which can be set with <code>control point number</code>. The distance for each particle is chosen randomly between <code>distance min</code> and <code>distance max</code>.  Also use this Initializer to place a particle at an exact position and just leave both distance values to 0. For more information about the other fields, lookup (<a href="./Function%20Library.md#position-within-sphere-random">Library</a>)</p>
</li>
<li>
<p><code>Position along Ring</code> - second most used positional initializer. Places new particles along a ring with a radius that can be set in <code>initial radius</code>. With a <code>thickness</code> greater than 0, the particles are randomly placed in a distance &lt; <code>thickness</code> around the “normal” ring position. Particles are randomly distrubuted around the ring. If you want to change this, check <code>even distribution</code>. This option forces all particles to spawn evenly spaced along the ring. With <code>even distribution count</code> you can control, how many particles are needed to place a full ring, otherwise (-1) they are spread based on the total particle count. (<a href="./Function%20Library.md#position-along-ring">Library</a>)</p>
</li>
<li>
<p><code>Position on path sequential</code> - Places new particles along a path between two control points. Therefor this initializer is often used for ropes, chains, etc. <code>start control point number</code> and <code>end control point number</code> define where particles are placed. <code>particles to map from start to end</code> is the number of particles needed to fill the path and <code>maximum distance</code> limits the length of the path, should the two CPs be too far away from each other. <code>use sequential CP pairs between start and end point</code> uses all CP numbers between your start and end as well, so it can be used to draw shapes like a square (with start, end, and 2 in between). (<a href="./Function%20Library.md#position-along-path-sequential">Library</a>)</p>
</li>
</ul>
<p>There are more positional Initializer, but they are mostly very specific and therefor explained when needed. However theres one more Initializer that is quite commonly used to place particles:</p>
<ul>
<li><code>Position modify offset random</code> - instead of spawning the particle at it’s position defined by a positional Initializer, the particles spawns in a random position around this point. <code>offset min</code> and <code>offset max</code> define the box where the particles are allowed to spawn in. (<a href="./Function%20Library.md#position-modify-offset-random">Library</a>)</li>
</ul>
<p>Another important use of Initializers are velocity generators. These can give particles a moving direction directly after they spawned. Velocity and movement in general are explained later.</p>
<h3 id="operator">Operator</h3>
<p>Operators are functions that have a persistent effect on all particles as long as they are alive. Together with Initializers, they create the main functionality of any effect.</p>
<p>One kind of operator should be used in every particle effect: a <strong>decay</strong> operator. Decay defines, how end when a particle you created is killed. If there’s no decay defined, the particle engine doesn’t know what to do with old particles and doesn’t delete them at all. to prevent this a warning message is displayed in the preview:<br>
<img src="https://i.imgur.com/SRRSIs6.png" alt=""></p>
<p>So we’ll have a look at the most common decay operator now:</p>
<ul>
<li><code>Lifespan decay</code> - This operator kills every particle, that has exceeded it’s lifetime. (<a href="./Function%20Library.md#lifespan-decay">Library</a>)</li>
</ul>
<p>So as described at the beginning, every particle has its own life duration. As long as this operator is active, the particle gets removed, when this duration is over. There aren’t much options for this operator, since its job is simple (yet very important). Note however, that if you want to have particles, that never die (ignoring lifetime), you can change the <code>operator end cap state</code> from -1 to 1 (endcap states in general are explained later).</p>
<p>All other decay operators have very specific use cases and will be explained as they are needed.</p>
<p>The next group of important operators are fades. They can have a great effect with little effort and are commonly used.</p>
<ul>
<li><code>Alpha fade in simple</code> - set’s the particles alpha value to 0 and increases it until it reaches the initial alpha value. The duration it takes can be defined in <code>proportional fade in time</code>, which is based on the particles lifetime. (<a href="./Function%20Library.md#alpha-fade-in-simple">Library</a>)</li>
<li><code>Alpha fade out simple</code> -  same as fade in, but reduces the alpha to 0 at the end of the lifetime. Fade out start time can be set with <code>proportional fade out time</code>.  (<a href="./Function%20Library.md#alpha-fade-out-simple">Library</a>)</li>
<li><code>Color fade</code> - continiously changes the particles color from its initial color towards <code>color fade</code>. Start and end time can be set with <code>fade start time</code> and <code>fade end time</code>, both are proportional to the particles lifetime. With <code>output field</code>, this operator can also scale other vector attributes of particles (but it’s rarely used).  (<a href="./Function%20Library.md#color-fade">Library</a>)</li>
<li><code>Radius scale</code> - basically not a fade, but it works similiar. Continously changes the radius of particles based on their lifetime. The scaling starts at <code>start scale</code> and is done at <code>end time</code>. The radius starts with <code>radius start scale</code> - times the initial value and ends with <code>radius end scale</code> - times the intial value. With <code>ease in and out</code> the linear scaling is replaced by a smoothed curve. <code>scale bias</code> also controls the scaling speed. A higher bias value (maximum is 1.0) will make the particles scale faster at the start and then smooth out.  (<a href="./Function%20Library.md#radius-scale">Library</a>)</li>
</ul>
<p>Another very useful and quite commonly used operator is:</p>
<ul>
<li><code>Movement lock to control point</code> -  moves all particles along with the movement of a control point, given by <code>control point number</code>. Everytime the CP is moved, the particles will move the same direction and distance. This will be at a 1 to 1 ratio (however it can be controller with the fading fields below, explanation when needed).  (<a href="./Function%20Library.md#movement-lock-to-control-point">Library</a>)</li>
</ul>
<p>There are also two operators, that enable a whole set of other operators, initializers and more. These two are:</p>
<ul>
<li><code>Rotation basic</code> - is needed for most actions that continuously change the rotation (roll, yaw, pitch) of particles. (<a href="./Function%20Library.md#rotation-basic">Library</a>)</li>
<li><code>Movement basic</code> - is needed for most functions that move particles, like velocities, forces etc. If you’d expect your particles to move, but they don’t, you should check if this operator is already added. It can also apply a gravity-like effect, which can be controlled with <code>gravity</code>. In most cases, only the z-coordinate is used and it can also have negative values. <code>drag</code> is a value, that controls how much your particles are slowed down over time, like friction does. With 0 drag, particles keep going with the same speed forever, a higher drag slows it down over time (1.0 is max). (<a href="./Function%20Library.md#movement-basic">Library</a>)</li>
</ul>
<p>There are many more oeprators that are really useful, but the most important ones were explained above. Additional operators will be explained whenever they are used in further tutorials.</p>
<h3 id="force-generator">Force Generator</h3>
<p>A force generator is a function that applies some kind of force to your particles in order to move them. <code>Movement basic</code> is required to use them. Using these is definatly more advanced at may be not obvious at first, but they can achieve great effects. The most used of them is shortly explained below:</p>
<ul>
<li><code>Pull towards control point</code> - constantly applies a force that pulls all particles closer to a given <code>control point number</code>. It can have negative <code>amount of force</code> to have an repulsive effect. This force is constantly added to the current velocity and results in steadily increasing speeds. The <code>falloff</code> power is similar to the drag from movement basic. Since the default value of it is 2, it (nearly) always needs to be redruced to make this force generator working. (<a href="./Function%20Library.md#pull-towards-control-point">Library</a>)</li>
</ul>
<h3 id="constraint">Constraint</h3>
<p>Constraints are the least used functions of all and may also have the biggest performance impact. However they are extremly potent and give access to very useful features. You should therefore only use it if you know exactly what you want to achieve with it. Some of them will be explained in further tutorials.</p>
<h3 id="renderer">Renderer</h3>
<p>All other functions we looked at earlier had an influence on invisible abstract particles, which are objects with properties like position, size, color etc.<br>
Renderers can now make these abstract particles visible to us. They decide whether we display single sparks, a long chain or even models. They aren’t necessary for each particle effect, but need to be added on every one that should be visible to user. Normally only one render is used, but there is no limit and multiple ones can be used at the same time, making use of these particle objects described above.</p>
<p>We’ll have a look at some common Renderers and important attributes of them:</p>
<ul>
<li>
<p><code>Render sprites</code> - most used “basic” Render. Displays a 2D plane with a sprite texture at the particles location, which always faces the camera, this way the effect of an 3D object is achieved.</p>
<ul>
<li>Further down in the properties, there’s <code>texture</code>, the most important field. If you press the little magnifying glass button, an asset browser window will open to choose a new texture for this sprite.</li>
<li><code>orientation type</code> sets the facing direction of the sprite. Normally this should be <code>Screen Align</code>, so it’s always facing the camera. But with <code>World-Z Align</code> or <code>Particle Normal Align</code> other effects can be achieved.</li>
<li><code>Color and alpga adjustments</code> is a collection of settings for color display related stuff and frequently changed. Since this is nearly the same for multiple Renderers, it will be explained later.</li>
<li><code>Radius Scale</code> multiplies the current radius for this specific sprite. Useful if multiple sprites Renderers are used at the same time.</li>
<li><code>Alpha Scale</code> is similiar to Radius Scale but for its alpha value.</li>
<li><code>Color blend</code> changes the color of this sprite (applied after all aother color changes through Initializers and Operators)</li>
<li>other properties might be explained as they’re needed</li>
<li>(<a href="./Function%20Library.md#render-sprites">Library</a>)</li>
</ul>
</li>
<li>
<p><code>Render rope</code> - used to draw a connected stretched texture that connects multiple particle objects. Attributes like radius, color, alpha, etc get interpolated between these points. Very useful for trails, ropes, chains, beams. It will connect in particle order based on particle indeces (can be viewed with the “Visualize” function described at the beginning)</p>
<ul>
<li>same as Render sprites in most ways</li>
<li><code>Closed loop</code> will connect the last with the first particle. Extremly useful in combination with the Position along ring Initializer</li>
<li><code>Reverse point order</code> will change the connection order from ascending to descending when checked (regarding particle indeces)</li>
<li><code>Texture Coordinates</code> is a collection of settings for displaying the texture, how its stretched etc. Also available on Render sprites, but more commonly used here. <code>texture V World Size</code>controls the stretch factor of the texture, it’s often good to increase this value the texture might feel compressed otherwise. <code>texture V Scroll Rate</code> adds a scrolling effect to the texture and can have great effect when the texture is seamless (and be more efficient than moving the particles)</li>
<li>(<a href="./Function%20Library.md#render-rope">Library</a>)</li>
</ul>
</li>
<li>
<p><code>Render models</code> - renderes a model at the particle positions. use it for small particle numbers. The models rendered are displayed but can’t be interacted with, so they can’t be selected, have no hitbox etc. However the behave visually the same as real world object, so they can be lighted and cast shadows.</p>
<ul>
<li>some fields from Render sprites can also be found here</li>
<li><code>models</code> is a list of models that are rendered. Empty on default, you can add new models by clicking on the + icon, expand the view and select a model in the opening asset browser.</li>
<li><code>material override</code> replaces the material the model uses with another one.</li>
<li><code>ignore normal</code> is the easiest solution to position your model upright if its lying on its side. Use this only if you don’t want to make further rotations with the model.</li>
<li><code>animated</code> can be checked to enable animations for the rendered model. A lot of other properties are tied to this setting. Will be explained more detailed later.</li>
<li><code>disable shadows</code> can be checked to disable shadows for this model</li>
<li>(<a href="./Function%20Library.md#render-models">Library</a>)</li>
</ul>
</li>
</ul>
<p>Important Note: Only one of these Renderers can be active per particle effect. If you want to have multiple models rendered, use multiple effects or add multiple models in the models field.</p>
<ul>
<li>
<p><code>Render sprite trail</code> - similar to a sprite in behavior, but dependend on the particle velocity. Note that particles might be invisible if you first add this Renderer as long as your particles don’t move. More speed of a particle stretches the lengh of the selected texture. They are very useful for trails (surprise!), but also streaks and other creative applications. They typically require the <code>trail length</code> property for the particles.</p>
<ul>
<li>mostly same as Render sprites</li>
<li><code>max length</code> is the maximum stretch length</li>
<li><code>min length</code> is the minimum stretch length</li>
<li><code>head / tail ...</code> color, alpha, radius scale for only this particle like in Render sprites. However can be seperatly set for the head and tail of the trail (interpolated in between).</li>
<li><code>ignore delta time</code> can be checked to simulate sprite trails velocity without actually moving them. Can be activated on most velocity Operators and Initializers as well (no Movement basic needed in this case).</li>
<li>(<a href="./Function%20Library.md#render-sprite-trail">Library</a>)</li>
</ul>
</li>
<li>
<p><code>Render deferred light</code> - renders a light source that casts a colored light around the particles. As it is only deferred light, no shadows will be casted. (<a href="./Function%20Library.md#render-deferred-light">Library</a>)</p>
</li>
<li>
<p><code>Render projected</code> -  renders a material on other objects like ground, trees etc. Will most likely be invisible in the Particle Editor, to avoid that go to the Controls Panel and clock on the “Browse” button in the center to select a model (it’s often useful to search for “ground” and select a plane model). Note here also that in contrast to all other texture based renderes this renderer requires a material (.vtex &lt;-&gt; .vmat). (<a href="./Function%20Library.md#render-projected">Library</a>)</p>
</li>
</ul>
<p>There are more renderers, but these were the most common ones.</p>
<h3 id="pre-emission-operator">Pre Emission Operator</h3>
<p>Under this category are operators, that are evaluated before all other Functions. They often manipulate CPs, manipulate children, etc. You won’t need them for most particle effects, but they can be a great addition and are vital for some complex particle behavior.</p>
<p>As most of them have pretty specific use cases, only the most common one will be explained right here:</p>
<ul>
<li><code>Set single control point position</code> - copies the coordinated of another control point to a new one. The new one can have an offset to the original one, described in <code>control point location</code>. This offset respects the orientation of the original control point and therefor is in local space. If you want to prevent this, check <code>set positions in world space</code>. The new CP will be continously recalculated when the original CP changes. If you want to prevent this, check <code>only set position once</code>. (<a href="./Function%20Library.md#set-single-control-point">Library</a>)</li>
<li><code>Set control point positions</code> -  basically the same as above, but can do 4 new CPs at once. (<a href="./Function%20Library.md#set-control-point-positions">Library</a>)</li>
</ul>
<p>Be aware that  when a control point is set by one of these Pre Emission Operators, they will be grayed out in the Controls Panel and cannot be changed manually anymore.</p>
<h2 id="what-now">What now?</h2>
<p>Now you should a basic understanding of the differences of the different Functions. But theres far more to learn that wasn’t covered here.</p>
<p>Now you could go and explore the Asset Browser, look up different particle effects, try to understand them and experiment as much as you like.</p>
<p>If you don’t want to figure out stuff by yourself, you can go on straight to the follow up tutorials. These will deepen your knowledge abd go more into detail for specif use cases and effects. So go checkout these links:</p>
<ul>
<li><a href="./Tutorials.md#guided-tutorial">Guided Tutorials</a></li>
</ul>

