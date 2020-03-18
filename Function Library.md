---


---

<p>save_header</p>
<p>back to the <a href="README.md">Overview</a>.</p>
<h1 id="function-library">Function Library</h1>
<p>A collection of all (the most) functions available and information about them. This data is auto-generated from different sources, so the data provided may not be 100% accurate.</p>
<h2 id="contents">Contents</h2>
<ul>
<li><a href="#operator">Operator</a>
<ul>
<li><a href="#lifespan-decay">Lifespan decay</a></li>
<li><a href="#radius-scale">Radius scale</a></li>
<li><a href="#movement-basic">Movement basic</a></li>
<li><a href="#alpha-fade-out-simple">Alpha fade out simple</a></li>
<li><a href="#alpha-fade-in-simple">Alpha fade in simple</a></li>
<li><a href="#color-fade">Color fade</a></li>
<li><a href="#movement-lock-to-control-point">Movement lock to control point</a></li>
<li><a href="#ramp-scalar-linear-simple">Ramp scalar linear simple</a></li>
<li><a href="#rotation-basic">Rotation basic</a></li>
<li><a href="#noise-vector">Noise vector</a></li>
<li><a href="#oscillate-vector">Oscillate vector</a></li>
<li><a href="#ramp-scalar-linear-random">Ramp scalar linear random</a></li>
<li><a href="#lifespan-endcap-timed-decay">Lifespan endcap timed decay</a></li>
<li><a href="#lerp-endcap-scalar">Lerp endcap scalar</a></li>
<li><a href="#alpha-fade-and-decay">Alpha fade and decay</a></li>
<li><a href="#movement-lock-to-bone">Movement lock to bone</a></li>
<li><a href="#oscillate-scalar">Oscillate scalar</a></li>
<li><a href="#alpha-fade-out-random">Alpha fade out random</a></li>
<li><a href="#remap-distance-to-control-point-to-scalar">Remap distance to control point to scalar</a></li>
<li><a href="#movement-skin-to-bones-rigid">Movement skin to bones rigid</a></li>
<li><a href="#inherit-attribute-from-parent-particle">Inherit attribute from parent particle</a></li>
<li><a href="#noise-scalar">Noise scalar</a></li>
<li><a href="#rotation-spin-roll">Rotation spin roll</a></li>
<li><a href="#movement-rotate-particle-around-axis">Movement rotate particle around axis</a></li>
<li><a href="#alpha-fade-in-random">Alpha fade in random</a></li>
<li><a href="#lifespan-minimum-alpha-decay">Lifespan minimum alpha decay</a></li>
<li><a href="#rotation-orient-relative-to-cp">Rotation orient relative to CP</a></li>
<li><a href="#ramp-scalar-spline-random">Ramp scalar spline random</a></li>
<li><a href="#movement-dampen-relative-to-control-point">Movement dampen relative to control point</a></li>
<li><a href="#movement-max-velocity">Movement max velocity</a></li>
<li><a href="#clamp-scalar">Clamp scalar</a></li>
<li><a href="#movement-set-to-control-point">Movement set to control point</a></li>
<li><a href="#oscillate-scalar-simple">Oscillate scalar simple</a></li>
<li><a href="#set-child-control-points-from-particle-positions">Set child control points from particle positions</a></li>
<li><a href="#cull-when-crossing-sphere">Cull when crossing sphere</a></li>
<li><a href="#movement-place-on-ground">Movement place on ground</a></li>
<li><a href="#set-control-points-from-particle-positions">Set control points from particle positions</a></li>
<li><a href="#set-per-child-control-point-from-particle-positions">Set per child control point from particle positions</a></li>
<li><a href="#lerp-initial-scalar">Lerp initial scalar</a></li>
<li><a href="#remap-speed-to-scalar">Remap speed to scalar</a></li>
<li><a href="#remap-control-point-to-scalar">Remap control point to scalar</a></li>
<li><a href="#remap-percentage-between-two-control-points-to-scalar-">Remap percentage between two control points to scalar </a></li>
<li><a href="#lifespan-minimum-radius-decay">Lifespan minimum radius decay</a></li>
<li><a href="#movement-maintain-positon-along-path">Movement maintain positon along path</a></li>
<li><a href="#set-float">Set Float</a></li>
<li><a href="#movement-skin-to-bones">Movement skin to bones</a></li>
<li><a href="#remap-direction-to-cp-to-vector">Remap direction to CP to vector</a></li>
<li><a href="#remap-control-point-to-vector">Remap control point to vector</a></li>
<li><a href="#movement-lock-to-saved-position-along-path">Movement lock to saved position along path</a></li>
<li><a href="#remap-velocity-to-vector">Remap velocity to vector</a></li>
<li><a href="#oscillate-vector-simple">Oscillate vector simple</a></li>
<li><a href="#ramp-scalar-spline-simple">Ramp scalar spline simple</a></li>
<li><a href="#inherit-attribute-from-parent-particle-1">Inherit attribute from parent particle</a></li>
<li><a href="#rotate-vector-random">Rotate vector random</a></li>
<li><a href="#movement-lerp-to-hitbox">Movement lerp to hitbox</a></li>
<li><a href="#remap-control-point-direction-to-vector">Remap control point direction to vector</a></li>
<li><a href="#rotation-orient-to-2d-direction">Rotation orient to 2d direction</a></li>
<li><a href="#color-fade-random">Color fade random</a></li>
<li><a href="#remap-scalar">Remap scalar</a></li>
<li><a href="#color-light-from-control-point">Color light from control point</a></li>
<li><a href="#set-cp-offset-to-cp-percentage-between-two-control-points">Set CP offset to CP percentage between two control points</a></li>
<li><a href="#rotation-from-cp-forward-orientation">Rotation from CP forward orientation</a></li>
<li><a href="#remap-cp-orientaton-to-rotations">Remap CP orientaton to rotations</a></li>
<li><a href="#lerp-endcap-vector">Lerp endcap vector</a></li>
<li><a href="#normalize-vector">Normalize vector</a></li>
<li><a href="#remap-distance-between-two-control-points-to-scalar">Remap distance between two control points to scalar</a></li>
<li><a href="#remap-distance-between-two-control-points-to-scalar-1">Remap distance between two control points to scalar</a></li>
<li><a href="#remap-game-visibility-scalar">Remap game visibility scalar</a></li>
<li><a href="#movement-loop-inside-sphere">Movement loop inside sphere</a></li>
<li><a href="#remap-particle-count-on-endcap-scalar">Remap particle count on endcap scalar</a></li>
<li><a href="#clamp-vector">Clamp vector</a></li>
<li><a href="#movement-match-particle-velocities">Movement match particle velocities</a></li>
<li><a href="#restart-effect-after-duration">Restart effect after duration</a></li>
<li><a href="#remap-game-visibility-of-cp-to-scalar-">Remap game visibility of CP to scalar </a></li>
<li><a href="#remap-difference-of-sequential-particle-vector-to-scalar">Remap difference of sequential particle vector to Scalar</a></li>
<li><a href="#remap-particle-count-to-scalar">Remap particle count to scalar</a></li>
<li><a href="#movement-maintain-offset">Movement maintain offset</a></li>
<li><a href="#set-cp-orientation-to-cp-direction">Set CP orientation to CP direction</a></li>
<li><a href="#cull-when-crossing-plane">Cull when crossing plane</a></li>
<li><a href="#remap-percentage-between-two-control-points-to-vector">Remap percentage between two control points to vector</a></li>
<li><a href="#remap-scalar-once-timed">Remap scalar once timed</a></li>
<li><a href="#cycle-scalar">Cycle Scalar</a></li>
<li><a href="#lifespan-from-endcap-decay">Lifespan from endcap decay</a></li>
<li><a href="#remap-vector-to-cp">Remap vector to CP</a></li>
<li><a href="#set-vec">Set Vec</a></li>
<li><a href="#lerp-initial-vector">Lerp initial vector</a></li>
<li><a href="#set-cp-orientation-to-ground-normal">Set CP orientation to ground normal</a></li>
<li><a href="#pin-particle-to-control-point">Pin Particle to control point</a></li>
<li><a href="#remap-dot-product-to-scalar">Remap dot product to scalar</a></li>
<li><a href="#movement-lock-to-saved-position-along-path-1">Movement lock to saved position along path</a></li>
<li><a href="#lifespan-maintain-count-decay-">Lifespan maintain count decay </a></li>
<li><a href="#reinitalize-on-endcap-scalar-random">Reinitalize on endcap scalar random</a></li>
<li><a href="#remap-cp-velocity-to-vector">Remap CP velocity to vector</a></li>
<li><a href="#set-vector-from-control-point">Set vector from control point</a></li>
<li><a href="#movement-lerp-to-initial-position-relative-to-cp">Movement Lerp to Initial Position relative to CP</a></li>
<li><a href="#calculate-vector-attribute">Calculate vector attribute</a></li>
<li><a href="#remap-on-endcap-scalar-">Remap on endcap scalar </a></li>
<li><a href="#remap-distance-to-line-between-2-control-points-to-vector">Remap distance to line between 2 control points to vector</a></li>
<li><a href="#remap-control-point-orientaton-to-rotation">Remap control point orientaton to rotation</a></li>
<li><a href="#remap-distance-to-line-between-2-control-points-to-scalar">Remap distance to line between 2 control points to scalar</a></li>
<li><a href="#remap-percentage-between-two-cps-to-lerp-cps-to-scalar">Remap percentage between two cps to lerp CPs to scalar</a></li>
<li><a href="#remap-control-point-to-velocity">Remap control point to velocity</a></li>
<li><a href="#point-vector-at-next-particle-position">Point vector at next particle position</a></li>
</ul>
</li>
<li><a href="#init">Init</a>
<ul>
<li><a href="#lifetime-random">Lifetime random</a></li>
<li><a href="#radius-random">Radius Random</a></li>
<li><a href="#rotation-random">Rotation random</a></li>
<li><a href="#color-random">Color Random</a></li>
<li><a href="#position-within-sphere-random">Position within sphere random</a></li>
<li><a href="#alpha-random">Alpha Random</a></li>
<li><a href="#position-modify-offset-random">Position modify offset random</a></li>
<li><a href="#sequence-random">Sequence Random</a></li>
<li><a href="#velocity-noise">Velocity noise</a></li>
<li><a href="#rotation-yaw-flip-random">Rotation yaw flip random</a></li>
<li><a href="#remap-particle-count-to-scalar-1">Remap particle count to scalar</a></li>
<li><a href="#rotation-speed-random">Rotation speed random</a></li>
<li><a href="#position-along-ring">Position along ring</a></li>
<li><a href="#remap-scalar-1">Remap scalar</a></li>
<li><a href="#trail-length-random">Trail length random</a></li>
<li><a href="#remap-control-point-to-scalar-1">Remap control point to scalar</a></li>
<li><a href="#position-from-parent-particles">Position from parent particles</a></li>
<li><a href="#position-modify-place-on-ground">Position modify place on ground</a></li>
<li><a href="#position-skin-to-bones-from-cp-snapshot">Position skin to bones from CP snapshot</a></li>
<li><a href="#rotation-yaw-random">Rotation yaw random</a></li>
<li><a href="#remap-noise-to-scalar">Remap noise to scalar</a></li>
<li><a href="#inherit-attribute-from-parent-particle-2">Inherit attribute from parent particle</a></li>
<li><a href="#position-modify-warp-random">Position modify warp random</a></li>
<li><a href="#velocity-random">Velocity random</a></li>
<li><a href="#position-along-path-sequential">Position along path sequential</a></li>
<li><a href="#remap-control-point-to-vector-1">Remap control point to vector</a></li>
<li><a href="#scalar-random">Scalar random</a></li>
<li><a href="#init-from-cp-snapshot">Init from CP snapshot</a></li>
<li><a href="#normal-align-to-cp">Normal align to CP</a></li>
<li><a href="#sequence-two-random">Sequence two random</a></li>
<li><a href="#velocity-inherit-from-control-point">Velocity inherit from control point</a></li>
<li><a href="#offset-vector-to-vector">Offset vector to vector</a></li>
<li><a href="#remap-initial-distance-to-control-point-to-scalar">Remap initial distance to control point to scalar</a></li>
<li><a href="#position-along-epitrochoid">Position along epitrochoid</a></li>
<li><a href="#init-from-killed-parent-particle">Init from killed parent particle</a></li>
<li><a href="#normal-lock-to-control-point">Normal lock to control point</a></li>
<li><a href="#remap-cp-orientation-to-rotation">Remap CP orientation to rotation</a></li>
<li><a href="#position-within-box-random">Position within box random</a></li>
<li><a href="#normal-modify-offset-random">Normal modify offset random</a></li>
<li><a href="#lifetime-from-sequence">Lifetime from sequence</a></li>
<li><a href="#remap-initial-direction-to-cp-to-vector">Remap initial direction to CP to vector</a></li>
<li><a href="#init-float">Init Float</a></li>
<li><a href="#velocity-set-from-control-point">Velocity set from control point</a></li>
<li><a href="#rotation-spin-yaw">Rotation spin yaw</a></li>
<li><a href="#vector-component-random">Vector component random</a></li>
<li><a href="#rotation-orient-relative-to-cp-1">Rotation orient relative to CP</a></li>
<li><a href="#init-status-effect">Init Status Effect</a></li>
<li><a href="#remap-scalar-to-vector">Remap scalar to vector</a></li>
<li><a href="#vector-random">Vector random</a></li>
<li><a href="#position-along-path-random">Position along path random</a></li>
<li><a href="#position-along-path-sequential-1">Position along path sequential</a></li>
<li><a href="#position-on-spiral-sphere">Position on spiral sphere</a></li>
<li><a href="#remap-qangie-in-cp-to-rotations">Remap QAngIe in CP to rotations</a></li>
<li><a href="#radius-from-cp-object">Radius from CP object</a></li>
<li><a href="#globally-scale-initial-attributes">Globally Scale Initial Attributes</a></li>
<li><a href="#set-hitbox-to-closest-hitbox">Set hitbox to closest hitbox</a></li>
<li><a href="#sequence-from-control-point">Sequence from control point</a></li>
<li><a href="#position-from-parent-cache-">Position from parent cache </a></li>
<li><a href="#cull-relative-to-ray-trace-environment-">Cull relative to ray trace environment </a></li>
<li><a href="#position-from-control-points">Position from control points</a></li>
<li><a href="#init-cp-orientation-to-rotations">Init CP orientation to rotations</a></li>
<li><a href="#init-vec">Init Vec</a></li>
<li><a href="#add-vector-to-vector">Add vector to vector</a></li>
<li><a href="#velocity-radial-random">Velocity radial random</a></li>
<li><a href="#remap-speed-to-scalar-1">Remap speed to scalar</a></li>
<li><a href="#lifetime-from-time-to-impact">Lifetime from time to impact</a></li>
<li><a href="#velocity-repulse-from-world">Velocity repulse from world</a></li>
<li><a href="#alpha-window-threshold-random">Alpha window threshold random</a></li>
<li><a href="#position-with-phyllotaxis-distribution">Position with phyllotaxis distribution</a></li>
<li><a href="#velocity-away-from-hitbox-random">Velocity away from hitbox random</a></li>
<li><a href="#position-modify-offset-relative-to-control-point">Position modify offset relative to control point</a></li>
<li><a href="#velocity-from-normal-random">Velocity from normal random</a></li>
<li><a href="#remap-initial-game-visibility-to-scalar">Remap initial game visibility to scalar</a></li>
<li><a href="#color-lit-per-particle">Color lit per particle</a></li>
<li><a href="#init-vector-attribute-from-a-list-of-values">Init vector attribute from a list of values</a></li>
<li><a href="#move-particles-between-2-control-points">Move particles between 2 control points</a></li>
<li><a href="#position-modify-warp-from-scalar">Position modify warp from scalar</a></li>
</ul>
</li>
<li><a href="#renderer">Renderer</a>
<ul>
<li><a href="#render-sprites">Render sprites</a></li>
<li><a href="#render-rope">Render rope</a></li>
<li><a href="#render-sprite-trail">Render sprite trail</a></li>
<li><a href="#render-deferred-light">Render deferred light</a></li>
<li><a href="#render-projected">Render projected</a></li>
<li><a href="#render-status-effect">Render Status Effect</a></li>
<li><a href="#render-screen-shake">Render screen shake</a></li>
<li><a href="#render-blobs">Render blobs</a></li>
<li><a href="#render-sound">Render sound</a></li>
<li><a href="#render-tree-shake">Render Tree Shake</a></li>
<li><a href="#render-text">Render Text</a></li>
</ul>
</li>
<li><a href="#emitter">Emitter</a>
<ul>
<li><a href="#emit-continuously">Emit continuously</a></li>
<li><a href="#emit-instantaniously">Emit instantaniously</a></li>
<li><a href="#emit-noise">Emit noise</a></li>
<li><a href="#emit-to-maintain-count">Emit to maintain count</a></li>
</ul>
</li>
<li><a href="#force-gen">Force-Gen</a>
<ul>
<li><a href="#pull-towards-control-point">Pull towards control point</a></li>
<li><a href="#random-force">Random force</a></li>
<li><a href="#twist-around-axis">Twist around axis</a></li>
<li><a href="#curlnoise-force">CurlNoise force</a></li>
<li><a href="#turbulent-force">Turbulent force</a></li>
<li><a href="#external-wind-force">External Wind force</a></li>
<li><a href="#local-acceleraton-force">Local acceleraton force</a></li>
<li><a href="#time-varying-force">Time varying force</a></li>
<li><a href="#force-based-on-distance-from-plane">Force based on distance from plane</a></li>
<li><a href="#create-vortices-from-parent-particles">Create vortices from parent particles</a></li>
</ul>
</li>
<li><a href="#pre">Pre</a>
<ul>
<li><a href="#set-single-control-point-position">Set single control point position</a></li>
<li><a href="#set-control-point-orientaton">Set control point orientaton</a></li>
<li><a href="#set-control-point-positions">Set control point Positions</a></li>
<li><a href="#set-per-child-control-point-from-parent-control-points">Set per child control point from parent control points</a></li>
<li><a href="#remap-cp-speed-to-cp">Remap CP speed to CP</a></li>
<li><a href="#hsv-shift-to-control-point">HSV Shift to control point</a></li>
<li><a href="#stop-effect-after-duraton">Stop effect after duraton</a></li>
<li><a href="#set-control-point-from-cp-object-scale">Set control point from CP object scale</a></li>
<li><a href="#set-control-point-rotation">Set control point rotation</a></li>
<li><a href="#set-control-point-to-random-position">Set control point to random Position</a></li>
<li><a href="#set-cp-orientaton-to-point-at-second-cp">Set CP orientaton to point at second CP</a></li>
<li><a href="#remap-average-scalar-value-to-cp">Remap average scalar value to CP</a></li>
<li><a href="#remap-cp-component-to-cp-component">Remap CP component to CP component</a></li>
<li><a href="#set-control-point-to-impact-point">Set control point to impact point</a></li>
<li><a href="#force-control-point-in-pet">Force Control Point In Pet</a></li>
<li><a href="#enable-children-from-parent-particle-count">Enable children from parent particle count</a></li>
<li><a href="#repeatedly-trigger-child-group">Repeatedly Trigger Child Group</a></li>
<li><a href="#set-control-point-component-to-scalar-expression">Set control point component to scalar expression</a></li>
<li><a href="#ramp-control-point-linear-random">Ramp control point linear random</a></li>
<li><a href="#use-random-children-in-group">Use Random Children in Group</a></li>
<li><a href="#set-dest-cp-field-1-if-source-cp-is-in-water-">Set dest CP field 1 if source CP is in water </a></li>
</ul>
</li>
<li><a href="#constraint">Constraint</a>
<ul>
<li><a href="#constrain-distance-to-control-point">Constrain distance to control point</a></li>
<li><a href="#collision-via-traces">Collision via traces</a></li>
<li><a href="#prevent-passing-through-a-plane">Prevent passing through a plane</a></li>
<li><a href="#constrain-distance-to-path-between-two-control-points">Constrain distance to path between two control points</a></li>
<li><a href="#constrain-particles-to-a-box">Constrain particles to a box</a></li>
<li><a href="#prevent-passing-through-static-part-of-world">Prevent passing through static part of world</a></li>
<li><a href="#rope-spring-constraint">Rope Spring constraint</a></li>
</ul>
</li>
</ul>
<h2 id="operator">Operator</h2>
<h3 id="lifespan-decay">Lifespan decay</h3>

<table>
<thead>
<tr>
<th>Lifespan decay</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_Decay</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>35435</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>This enables particles to be destroyed by the effect.</p><p>All effects should have a Decay Operator (usually Lifespan Decay) unless you’re certain that the particles will get destroyed by some other means (usually code.)</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rope decay</td>
<td>boolean</td>
</tr>
<tr>
<td>notes</td>
<td>string</td>
</tr>
</tbody>
</table><h3 id="radius-scale">Radius scale</h3>

<table>
<thead>
<tr>
<th>Radius scale</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_InterpolateRadius</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>32380</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Scales particles from the start to end scale over the specified time. Multiple Radius Scale operators can be used in an effect as long as their time coverage doesn’t overlap.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>bias</td>
<td>float</td>
</tr>
<tr>
<td>end scale</td>
<td>float</td>
</tr>
<tr>
<td>start scale</td>
<td>float</td>
</tr>
<tr>
<td>end time</td>
<td>float</td>
</tr>
<tr>
<td>start time</td>
<td>float</td>
</tr>
<tr>
<td>ease in and out</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="movement-basic">Movement basic</h3>

<table>
<thead>
<tr>
<th>Movement basic</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_BasicMovement</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>29027</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Enables basic movement for particles. (“Basic” in the sense of <i>fundamental</i> rather than simplistic.)</p><p>It’s not a bad idea to always add Movement Basic to new effects; if it ends up being spatially static later, you can remove the Operator for a tiny performance gain.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>gravity</td>
<td>vector</td>
<td>Gravitational effect on the particles.</td>
</tr>
<tr>
<td>drag</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>max constraint passes</td>
<td>integer</td>
<td></td>
</tr>
</tbody>
</table><h3 id="alpha-fade-out-simple">Alpha fade out simple</h3>

<table>
<thead>
<tr>
<th>Alpha fade out simple</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_FadeOutSimple</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>23380</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Fades particles out over time.</p><p><b>proportional fade out time</b> is a percentage of the particle’s lifetime, expressed as a range between 0 and 1. (So a setting of 0.25 on a particle with a 4-second lifetime would start fading out 3 seconds after being emitted, and would take 1 second to fade out completely.)</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>fade out time</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="alpha-fade-in-simple">Alpha fade in simple</h3>

<table>
<thead>
<tr>
<th>Alpha fade in simple</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_FadeInSimple</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>18427</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Fades particles in over time.</p><p><b>proportional fade in time</b> is a percentage of the particle’s lifetime, expressed as a range between 0 and 1. (So a setting of 0.5 on a particle with a 4-second lifetime would take 2 seconds to fade in completely.)</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>fade in time</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="color-fade">Color fade</h3>

<table>
<thead>
<tr>
<th>Color fade</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_ColorInterpolate</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>15575</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Within the specified time, each particle fades from its color at <b>fade_start_time</b> to <b>color_fade</b>.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>color fade</td>
<td>vector</td>
</tr>
<tr>
<td>fade start time</td>
<td>float</td>
</tr>
<tr>
<td>fade end time</td>
<td>float</td>
</tr>
<tr>
<td>ease in out</td>
<td>boolean</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>notes</td>
<td>string</td>
</tr>
</tbody>
</table><h3 id="movement-lock-to-control-point">Movement lock to control point</h3>

<table>
<thead>
<tr>
<th>Movement lock to control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_PositionLock</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>15184</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>Causes particles to inherit the movement (and optionally rotation) of a control point.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>start time_max</td>
<td>float</td>
</tr>
<tr>
<td>start time_min</td>
<td>float</td>
</tr>
<tr>
<td>end time_min</td>
<td>float</td>
</tr>
<tr>
<td>lock rot</td>
<td>boolean</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>range</td>
<td>float</td>
</tr>
<tr>
<td>end time_max</td>
<td>float</td>
</tr>
<tr>
<td>jump threshold</td>
<td>float</td>
</tr>
<tr>
<td>prev pos scale</td>
<td>float</td>
</tr>
<tr>
<td>end time_exp</td>
<td>float</td>
</tr>
<tr>
<td>start time_exp</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="ramp-scalar-linear-simple">Ramp scalar linear simple</h3>

<table>
<thead>
<tr>
<th>Ramp scalar linear simple</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RampScalarLinearSimple</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>9981</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>field</td>
<td>integer</td>
</tr>
<tr>
<td>rate</td>
<td>string</td>
</tr>
<tr>
<td>end time</td>
<td>float</td>
</tr>
<tr>
<td>start time</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="rotation-basic">Rotation basic</h3>

<table>
<thead>
<tr>
<th>Rotation basic</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SpinUpdate</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>7096</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>This simply enables rotation through the effect’s Base Properties (<b>rotation_speed</b>) or through the initializer “Rotation Speed Random”.</p><p>Particle rotation can also be achieved with the operators “Rotation Spin Roll” and “Rotation Spin Yaw”, which do not require the “Rotation Basic” operator.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody></tbody>
</table><h3 id="noise-vector">Noise vector</h3>

<table>
<thead>
<tr>
<th>Noise vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_VectorNoise</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>5003</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Remaps a noise function to any exposed vector. The noise function is mapped based on both time and space, each with their own coordinate scales and offsets.</p><p>This creates a range of results that are non-random but vary based on creation time and position.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>output max</td>
<td>vector</td>
</tr>
<tr>
<td>output min</td>
<td>vector</td>
</tr>
<tr>
<td>noise scale</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>use additive blending</td>
<td>boolean</td>
</tr>
<tr>
<td>offset</td>
<td>boolean</td>
</tr>
<tr>
<td>noise animation time scale</td>
<td>float</td>
</tr>
<tr>
<td>notes</td>
<td>string</td>
</tr>
<tr>
<td>normalize to stop time</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="oscillate-vector">Oscillate vector</h3>

<table>
<thead>
<tr>
<th>Oscillate vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_OscillateVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>3375</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rate min</td>
<td>vector</td>
</tr>
<tr>
<td>rate max</td>
<td>vector</td>
</tr>
<tr>
<td>frequency min</td>
<td>vector</td>
</tr>
<tr>
<td>frequency max</td>
<td>vector</td>
</tr>
<tr>
<td>proportional</td>
<td>boolean</td>
</tr>
<tr>
<td>end time_min</td>
<td>float</td>
</tr>
<tr>
<td>start time_max</td>
<td>float</td>
</tr>
<tr>
<td>start time_min</td>
<td>float</td>
</tr>
<tr>
<td>osc add</td>
<td>float</td>
</tr>
<tr>
<td>field</td>
<td>integer</td>
</tr>
<tr>
<td>offset</td>
<td>boolean</td>
</tr>
<tr>
<td>end time_max</td>
<td>float</td>
</tr>
<tr>
<td>osc mult</td>
<td>float</td>
</tr>
<tr>
<td>proportional op</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="ramp-scalar-linear-random">Ramp scalar linear random</h3>

<table>
<thead>
<tr>
<th>Ramp scalar linear random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RampScalarLinear</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>3117</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>field</td>
<td>integer</td>
</tr>
<tr>
<td>rate max</td>
<td>string</td>
</tr>
<tr>
<td>rate min</td>
<td>string</td>
</tr>
<tr>
<td>end time_min</td>
<td>float</td>
</tr>
<tr>
<td>end time_max</td>
<td>float</td>
</tr>
<tr>
<td>proportional op</td>
<td>boolean</td>
</tr>
<tr>
<td>start time_max</td>
<td>float</td>
</tr>
<tr>
<td>start time_min</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="lifespan-endcap-timed-decay">Lifespan endcap timed decay</h3>

<table>
<thead>
<tr>
<th>Lifespan endcap timed decay</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_EndCapTimedDecay</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2893</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>decay time</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="lerp-endcap-scalar">Lerp endcap scalar</h3>

<table>
<thead>
<tr>
<th>Lerp endcap scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_LerpEndCapScalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2506</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>output</td>
<td>float</td>
</tr>
<tr>
<td>lerp time</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="alpha-fade-and-decay">Alpha fade and decay</h3>

<table>
<thead>
<tr>
<th>Alpha fade and decay</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_FadeAndKill</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2355</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Essentially combines the three operators “Lifespan Decay”, “Alpha Fade In Simple”, and “Alpha Fade Out Simple”.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>start alpha</td>
<td>float</td>
</tr>
<tr>
<td>end fade in time</td>
<td>float</td>
</tr>
<tr>
<td>start fade out time</td>
<td>float</td>
</tr>
<tr>
<td>end fade out time</td>
<td>float</td>
</tr>
<tr>
<td>end alpha</td>
<td>float</td>
</tr>
<tr>
<td>start fade in time</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="movement-lock-to-bone">Movement lock to bone</h3>

<table>
<thead>
<tr>
<th>Movement lock to bone</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_LockToBone</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2344</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>life time fade end</td>
<td>float</td>
</tr>
<tr>
<td>life time fade start</td>
<td>float</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>hitbox set name</td>
<td>string</td>
</tr>
<tr>
<td>use bones</td>
<td>boolean</td>
</tr>
<tr>
<td>rigid</td>
<td>boolean</td>
</tr>
<tr>
<td>jump threshold</td>
<td>float</td>
</tr>
<tr>
<td>prev pos scale</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="oscillate-scalar">Oscillate scalar</h3>

<table>
<thead>
<tr>
<th>Oscillate scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_OscillateScalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2253</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>osc add</td>
<td>float</td>
</tr>
<tr>
<td>osc mult</td>
<td>float</td>
</tr>
<tr>
<td>end time_max</td>
<td>float</td>
</tr>
<tr>
<td>end time_min</td>
<td>float</td>
</tr>
<tr>
<td>frequency max</td>
<td>string</td>
</tr>
<tr>
<td>frequency min</td>
<td>string</td>
</tr>
<tr>
<td>rate max</td>
<td>string</td>
</tr>
<tr>
<td>rate min</td>
<td>string</td>
</tr>
<tr>
<td>proportional</td>
<td>boolean</td>
</tr>
<tr>
<td>field</td>
<td>integer</td>
</tr>
<tr>
<td>proportional op</td>
<td>boolean</td>
</tr>
<tr>
<td>start time_max</td>
<td>float</td>
</tr>
<tr>
<td>start time_min</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="alpha-fade-out-random">Alpha fade out random</h3>

<table>
<thead>
<tr>
<th>Alpha fade out random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_FadeOut</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2231</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Fades particles out over a random period of time within the specified range.</p><p>Unlike “Alpha Fade Out Simple”, this operator has an option to define your range in seconds rather than a percentage of the particle’s lifespan. To use seconds, simply turn the <b>proportional</b> property off.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>fade out time min</td>
<td>float</td>
</tr>
<tr>
<td>fade out time max</td>
<td>float</td>
</tr>
<tr>
<td>proportional</td>
<td>boolean</td>
</tr>
<tr>
<td>ease in and out</td>
<td>boolean</td>
</tr>
<tr>
<td>fade bias</td>
<td>float</td>
</tr>
<tr>
<td>fade out time exp</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="remap-distance-to-control-point-to-scalar">Remap distance to control point to scalar</h3>

<table>
<thead>
<tr>
<th>Remap distance to control point to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_DistanceToCP</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1566</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>scale initial range</td>
<td>boolean</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>input min</td>
<td>float</td>
</tr>
<tr>
<td>start CP</td>
<td>integer</td>
</tr>
<tr>
<td>scale current</td>
<td>boolean</td>
</tr>
<tr>
<td>active range</td>
<td>boolean</td>
</tr>
<tr>
<td>set method</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="movement-skin-to-bones-rigid">Movement skin to bones rigid</h3>

<table>
<thead>
<tr>
<th>Movement skin to bones rigid</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SnapshotRigidSkinToBones</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1536</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>transform normals</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="inherit-attribute-from-parent-particle">Inherit attribute from parent particle</h3>

<table>
<thead>
<tr>
<th>Inherit attribute from parent particle</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_InheritFromParentParticles</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1385</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Assigns a parent particle’s attribute to each particle within the system.</p><p>This differs from the initializer “Inherit Initial Value from Parent Particle” in that the parent’s attribute will be inherited every frame in real-time.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>scale</td>
<td>float</td>
</tr>
<tr>
<td>increment</td>
<td>integer</td>
</tr>
<tr>
<td>random distribution</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="noise-scalar">Noise scalar</h3>

<table>
<thead>
<tr>
<th>Noise scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_Noise</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1337</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Remaps a noise function to any exposed scalar. The noise function is mapped based on both time and space, each with their own coordinate scales and offsets.</p><p>This creates a range of results that are non-random but vary based on creation time and position.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>noise scale</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>use additive blending</td>
<td>boolean</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>noise animation time scale</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="rotation-spin-roll">Rotation spin roll</h3>

<table>
<thead>
<tr>
<th>Rotation spin roll</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_Spin</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1283</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Rotates each particle along the “roll” axis.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>spin rate stop time</td>
<td>float</td>
</tr>
<tr>
<td>spin rate degrees</td>
<td>integer</td>
</tr>
<tr>
<td>spin rate min degrees</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="movement-rotate-particle-around-axis">Movement rotate particle around axis</h3>

<table>
<thead>
<tr>
<th>Movement rotate particle around axis</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_MovementRotateParticleAroundAxis</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1230</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>rot rate</td>
<td>float</td>
</tr>
<tr>
<td>use local space</td>
<td>boolean</td>
</tr>
<tr>
<td>rot axis</td>
<td>vector</td>
</tr>
</tbody>
</table><h3 id="alpha-fade-in-random">Alpha fade in random</h3>

<table>
<thead>
<tr>
<th>Alpha fade in random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_FadeIn</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1064</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Fades particles in over a random period of time within the specified range.</p><p>Unlike “Alpha Fade In Simple”, this operator has an option to define your range in seconds rather than a percentage of the particle’s lifespan. To use seconds, simply turn the <b>proportional</b> property off.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>proportional</td>
<td>boolean</td>
</tr>
<tr>
<td>fade in time max</td>
<td>float</td>
</tr>
<tr>
<td>fade in time min</td>
<td>float</td>
</tr>
<tr>
<td>fade in time exp</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="lifespan-minimum-alpha-decay">Lifespan minimum alpha decay</h3>

<table>
<thead>
<tr>
<th>Lifespan minimum alpha decay</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_AlphaDecay</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1047</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>min alpha</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="rotation-orient-relative-to-cp">Rotation orient relative to CP</h3>

<table>
<thead>
<tr>
<th>Rotation orient relative to CP</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_Orient2DRelToCP</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>985</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rot offset</td>
<td>float</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>spin strength</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="ramp-scalar-spline-random">Ramp scalar spline random</h3>

<table>
<thead>
<tr>
<th>Ramp scalar spline random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RampScalarSpline</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>978</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rate max</td>
<td>string</td>
</tr>
<tr>
<td>field</td>
<td>integer</td>
</tr>
<tr>
<td>rate min</td>
<td>string</td>
</tr>
<tr>
<td>bias</td>
<td>float</td>
</tr>
<tr>
<td>ease out</td>
<td>boolean</td>
</tr>
<tr>
<td>end time_max</td>
<td>float</td>
</tr>
<tr>
<td>end time_min</td>
<td>float</td>
</tr>
<tr>
<td>start time_min</td>
<td>float</td>
</tr>
<tr>
<td>start time_max</td>
<td>float</td>
</tr>
<tr>
<td>proportional op</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="movement-dampen-relative-to-control-point">Movement dampen relative to control point</h3>

<table>
<thead>
<tr>
<th>Movement dampen relative to control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_DampenToCP</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>896</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Drains a particle’s internal velocity as it approaches the specified control point. If no other forces are acting on it, the particle will eventually stop.</p><p>This can be used with operator “Movement Lock to Control Point” (and its distance fade property) to have a control point “capture” particles near it then draw them along. It can also lock endpoints of a line of particles while allowing the middle section to move freely.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>range</td>
<td>float</td>
</tr>
<tr>
<td>scale</td>
<td>float</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="movement-max-velocity">Movement max velocity</h3>

<table>
<thead>
<tr>
<th>Movement max velocity</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_MaxVelocity</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>871</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>override CP</td>
<td>integer</td>
</tr>
<tr>
<td>max velocity</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="clamp-scalar">Clamp scalar</h3>

<table>
<thead>
<tr>
<th>Clamp scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_ClampScalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>826</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Limits the specified scalar’s value to a range between <b>output minimum</b> and <b>output maximum</b>.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="movement-set-to-control-point">Movement set to control point</h3>

<table>
<thead>
<tr>
<th>Movement set to control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetToCP</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>782</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>offset</td>
<td>vector</td>
</tr>
<tr>
<td>offset local</td>
<td>boolean</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="oscillate-scalar-simple">Oscillate scalar simple</h3>

<table>
<thead>
<tr>
<th>Oscillate scalar simple</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_OscillateScalarSimple</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>737</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>osc add</td>
<td>float</td>
</tr>
<tr>
<td>frequency</td>
<td>string</td>
</tr>
<tr>
<td>rate</td>
<td>string</td>
</tr>
<tr>
<td>field</td>
<td>integer</td>
</tr>
<tr>
<td>osc mult</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="set-child-control-points-from-particle-positions">Set child control points from particle positions</h3>

<table>
<thead>
<tr>
<th>Set child control points from particle positions</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetChildControlPoints</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>685</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>first control point</td>
<td>integer</td>
</tr>
<tr>
<td>set orientation</td>
<td>boolean</td>
</tr>
<tr>
<td>num control points</td>
<td>integer</td>
</tr>
<tr>
<td>first source point</td>
<td>integer</td>
</tr>
<tr>
<td>child group ID</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="cull-when-crossing-sphere">Cull when crossing sphere</h3>

<table>
<thead>
<tr>
<th>Cull when crossing sphere</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_DistanceCull</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>676</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Instantly destroys particles when they pass the specified spherical threshold.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>control point</td>
<td>integer</td>
</tr>
<tr>
<td>distance</td>
<td>float</td>
</tr>
<tr>
<td>point offset</td>
<td>vector</td>
</tr>
<tr>
<td>cull inside</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="movement-place-on-ground">Movement place on ground</h3>

<table>
<thead>
<tr>
<th>Movement place on ground</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_MovementPlaceOnGround</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>632</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>if ( m_nRefCP1 &gt; -1 ){	if ( ( pParticles-&gt;GetControlPointAtCurrentTime( m_nRefCP1 ) - pCtx-&gt;m_vecPrevPos1 ).Length() &gt; m_flTolerance )	{		bDirty = true;		pCtx-&gt;m_vecPrevPos1 = pParticles-&gt;GetControlPointAtCurrentTime( m_nRefCP1 );		pCtx-&gt;m_flLerpTime = pParticles-&gt;m_flCurTime;	}}</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>offset</td>
<td>float</td>
</tr>
<tr>
<td>max trace length</td>
<td>float</td>
</tr>
<tr>
<td>tolerance</td>
<td>float</td>
</tr>
<tr>
<td>trace offset</td>
<td>float</td>
</tr>
<tr>
<td>collision group name</td>
<td>string</td>
</tr>
<tr>
<td>include water</td>
<td>boolean</td>
</tr>
<tr>
<td>lerp CP</td>
<td>integer</td>
</tr>
<tr>
<td>ref CP1</td>
<td>integer</td>
</tr>
<tr>
<td>lerp rate</td>
<td>float</td>
</tr>
<tr>
<td>set normal</td>
<td>boolean</td>
</tr>
<tr>
<td>kill</td>
<td>boolean</td>
</tr>
<tr>
<td>scale offset</td>
<td>boolean</td>
</tr>
<tr>
<td>ref CP2</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="set-control-points-from-particle-positions">Set control points from particle positions</h3>

<table>
<thead>
<tr>
<th>Set control points from particle positions</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetControlPointsToParticle</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>590</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>first control point</td>
<td>integer</td>
</tr>
<tr>
<td>set orientation</td>
<td>boolean</td>
</tr>
<tr>
<td>first source point</td>
<td>integer</td>
</tr>
<tr>
<td>num control points</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="set-per-child-control-point-from-particle-positions">Set per child control point from particle positions</h3>

<table>
<thead>
<tr>
<th>Set per child control point from particle positions</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetPerChildControlPoint</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>575</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>num control points</td>
<td>integer</td>
</tr>
<tr>
<td>first control point</td>
<td>integer</td>
</tr>
<tr>
<td>set orientation</td>
<td>boolean</td>
</tr>
<tr>
<td>num based on particle count</td>
<td>boolean</td>
</tr>
<tr>
<td>child group ID</td>
<td>integer</td>
</tr>
<tr>
<td>particle increment</td>
<td>integer</td>
</tr>
<tr>
<td>first source point</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="lerp-initial-scalar">Lerp initial scalar</h3>

<table>
<thead>
<tr>
<th>Lerp initial scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_LerpScalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>506</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>end time</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>output</td>
<td>float</td>
</tr>
<tr>
<td>start time</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="remap-speed-to-scalar">Remap speed to scalar</h3>

<table>
<thead>
<tr>
<th>Remap speed to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapSpeed</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>501</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>scale current</td>
<td>boolean</td>
</tr>
<tr>
<td>input min</td>
<td>float</td>
</tr>
<tr>
<td>ignore delta</td>
<td>boolean</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>scale initial range</td>
<td>boolean</td>
</tr>
<tr>
<td>set method</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="remap-control-point-to-scalar">Remap control point to scalar</h3>

<table>
<thead>
<tr>
<th>Remap control point to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapCPtoScalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>479</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>CP input</td>
<td>integer</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>field</td>
<td>integer</td>
</tr>
<tr>
<td>scale initial range</td>
<td>boolean</td>
</tr>
<tr>
<td>input min</td>
<td>float</td>
</tr>
<tr>
<td>scale current</td>
<td>boolean</td>
</tr>
<tr>
<td>set method</td>
<td>integer</td>
</tr>
<tr>
<td>interp rate</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="remap-percentage-between-two-control-points-to-scalar">Remap percentage between two control points to scalar</h3>

<table>
<thead>
<tr>
<th>Remap percentage between two control points to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_PercentageBetweenCPs</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>472</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>scale current</td>
<td>boolean</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>input min</td>
<td>float</td>
</tr>
<tr>
<td>scale initial range</td>
<td>boolean</td>
</tr>
<tr>
<td>start CP</td>
<td>integer</td>
</tr>
<tr>
<td>end CP</td>
<td>integer</td>
</tr>
<tr>
<td>set method</td>
<td>integer</td>
</tr>
<tr>
<td>active range</td>
<td>boolean</td>
</tr>
<tr>
<td>radial check</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="lifespan-minimum-radius-decay">Lifespan minimum radius decay</h3>

<table>
<thead>
<tr>
<th>Lifespan minimum radius decay</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RadiusDecay</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>427</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>min radius</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="movement-maintain-positon-along-path">Movement maintain positon along path</h3>

<table>
<thead>
<tr>
<th>Movement maintain positon along path</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_MaintainSequentialPath</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>411</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>num to assign</td>
<td>float</td>
</tr>
<tr>
<td>path params</td>
<td>path params (special)</td>
</tr>
<tr>
<td>max distance</td>
<td>float</td>
</tr>
<tr>
<td>cohesion strength</td>
<td>float</td>
</tr>
<tr>
<td>use particle count</td>
<td>boolean</td>
</tr>
<tr>
<td>tolerance</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="set-float">Set Float</h3>

<table>
<thead>
<tr>
<th>Set Float</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetFloat</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>397</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>input value</td>
<td>float (special)</td>
</tr>
<tr>
<td>output field</td>
<td>integer</td>
</tr>
<tr>
<td>scale initial value</td>
<td>boolean</td>
</tr>
<tr>
<td>set method</td>
<td>integer</td>
</tr>
<tr>
<td>lerp</td>
<td>float (special)</td>
</tr>
<tr>
<td>normalize to stop time</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="movement-skin-to-bones">Movement skin to bones</h3>

<table>
<thead>
<tr>
<th>Movement skin to bones</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SnapshotSkinToBones</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>377</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>life time fade start</td>
<td>float</td>
</tr>
<tr>
<td>life time fade end</td>
<td>float</td>
</tr>
<tr>
<td>transform normals</td>
<td>boolean</td>
</tr>
<tr>
<td>prev pos scale</td>
<td>float</td>
</tr>
<tr>
<td>jump threshold</td>
<td>float</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="remap-direction-to-cp-to-vector">Remap direction to CP to vector</h3>

<table>
<thead>
<tr>
<th>Remap direction to CP to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapDirectionToCPToVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>370</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>normalize</td>
<td>boolean</td>
</tr>
<tr>
<td>offset of rotation</td>
<td>float</td>
</tr>
<tr>
<td>offset axis</td>
<td>vector</td>
</tr>
<tr>
<td>scale</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="remap-control-point-to-vector">Remap control point to vector</h3>

<table>
<thead>
<tr>
<th>Remap control point to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapCPtoVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>328</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>CP input</td>
<td>integer</td>
</tr>
<tr>
<td>input max</td>
<td>vector</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>output max</td>
<td>vector</td>
</tr>
<tr>
<td>output min</td>
<td>vector</td>
</tr>
<tr>
<td>scale initial range</td>
<td>boolean</td>
</tr>
<tr>
<td>interp rate</td>
<td>float</td>
</tr>
<tr>
<td>input min</td>
<td>vector</td>
</tr>
<tr>
<td>scale current</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="movement-lock-to-saved-position-along-path">Movement lock to saved position along path</h3>

<table>
<thead>
<tr>
<th>Movement lock to saved position along path</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_LockToSavedSequentialPath</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>283</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>path params</td>
<td>path params (special)</td>
</tr>
<tr>
<td>CP pairs</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="remap-velocity-to-vector">Remap velocity to vector</h3>

<table>
<thead>
<tr>
<th>Remap velocity to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapVelocityToVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>255</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>normalize</td>
<td>boolean</td>
</tr>
<tr>
<td>scale</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="oscillate-vector-simple">Oscillate vector simple</h3>

<table>
<thead>
<tr>
<th>Oscillate vector simple</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_OscillateVectorSimple</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>239</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>frequency</td>
<td>vector</td>
</tr>
<tr>
<td>rate</td>
<td>vector</td>
</tr>
<tr>
<td>offset</td>
<td>boolean</td>
</tr>
<tr>
<td>osc add</td>
<td>float</td>
</tr>
<tr>
<td>osc mult</td>
<td>float</td>
</tr>
<tr>
<td>field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="ramp-scalar-spline-simple">Ramp scalar spline simple</h3>

<table>
<thead>
<tr>
<th>Ramp scalar spline simple</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RampScalarSplineSimple</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>229</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>field</td>
<td>integer</td>
</tr>
<tr>
<td>ease out</td>
<td>boolean</td>
</tr>
<tr>
<td>end time</td>
<td>float</td>
</tr>
<tr>
<td>rate</td>
<td>string</td>
</tr>
<tr>
<td>start time</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="inherit-attribute-from-parent-particle-1">Inherit attribute from parent particle</h3>

<table>
<thead>
<tr>
<th>Inherit attribute from parent particle</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_InheritFromParentParticlesV2</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>222</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>increment</td>
<td>integer</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>missing parent behavior</td>
<td>integer</td>
</tr>
<tr>
<td>scale</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="rotate-vector-random">Rotate vector random</h3>

<table>
<thead>
<tr>
<th>Rotate vector random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RotateVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>220</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rot rate max</td>
<td>float</td>
</tr>
<tr>
<td>rot axis max</td>
<td>vector</td>
</tr>
<tr>
<td>rot axis min</td>
<td>vector</td>
</tr>
<tr>
<td>rot rate min</td>
<td>float</td>
</tr>
<tr>
<td>normalize</td>
<td>boolean</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="movement-lerp-to-hitbox">Movement lerp to hitbox</h3>

<table>
<thead>
<tr>
<th>Movement lerp to hitbox</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_MoveToHitbox</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>185</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>life time lerp end</td>
<td>float</td>
</tr>
<tr>
<td>life time lerp start</td>
<td>float</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>prev pos scale</td>
<td>float</td>
</tr>
<tr>
<td>hitbox set name</td>
<td>string</td>
</tr>
</tbody>
</table><h3 id="remap-control-point-direction-to-vector">Remap control point direction to vector</h3>

<table>
<thead>
<tr>
<th>Remap control point direction to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapControlPointDirectionToVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>172</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="rotation-orient-to-2d-direction">Rotation orient to 2d direction</h3>

<table>
<thead>
<tr>
<th>Rotation orient to 2d direction</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_OrientTo2dDirection</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>172</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rot offset</td>
<td>float</td>
</tr>
<tr>
<td>spin strength</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="color-fade-random">Color fade random</h3>

<table>
<thead>
<tr>
<th>Color fade random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_ColorInterpolateRandom</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>169</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>color fade min</td>
<td>vector</td>
</tr>
<tr>
<td>color fade max</td>
<td>vector</td>
</tr>
<tr>
<td>fade end time</td>
<td>float</td>
</tr>
<tr>
<td>fade start time</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="remap-scalar">Remap scalar</h3>

<table>
<thead>
<tr>
<th>Remap scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapScalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>162</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Remaps any exposed scalar’s value to any other scalar on an ongoing basis.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>field input</td>
<td>integer</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>input min</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="color-light-from-control-point">Color light from control point</h3>

<table>
<thead>
<tr>
<th>Color light from control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_ControlpointLight</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>161</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>light color 1</td>
<td>vector</td>
</tr>
<tr>
<td>control point 1</td>
<td>integer</td>
</tr>
<tr>
<td>light fifty dist 1</td>
<td>string</td>
</tr>
<tr>
<td>use normal</td>
<td>boolean</td>
</tr>
<tr>
<td>light zero dist 1</td>
<td>string</td>
</tr>
<tr>
<td>CP offset 1</td>
<td>vector</td>
</tr>
<tr>
<td>use H lambert</td>
<td>boolean</td>
</tr>
<tr>
<td>control point 2</td>
<td>integer</td>
</tr>
<tr>
<td>CP offset 2</td>
<td>vector</td>
</tr>
<tr>
<td>light fifty dist 2</td>
<td>string</td>
</tr>
<tr>
<td>light zero dist 2</td>
<td>string</td>
</tr>
<tr>
<td>light color 2</td>
<td>vector</td>
</tr>
<tr>
<td>light fifty dist 3</td>
<td>string</td>
</tr>
<tr>
<td>light zero dist 3</td>
<td>string</td>
</tr>
<tr>
<td>light fifty dist 4</td>
<td>string</td>
</tr>
<tr>
<td>light zero dist 4</td>
<td>string</td>
</tr>
<tr>
<td>light color 3</td>
<td>vector</td>
</tr>
<tr>
<td>light color 4</td>
<td>vector</td>
</tr>
<tr>
<td>control point 3</td>
<td>integer</td>
</tr>
<tr>
<td>control point 4</td>
<td>integer</td>
</tr>
<tr>
<td>clamp lower range</td>
<td>boolean</td>
</tr>
<tr>
<td>CP offset 4</td>
<td>vector</td>
</tr>
<tr>
<td>CP offset 3</td>
<td>vector</td>
</tr>
<tr>
<td>scale</td>
<td>float</td>
</tr>
<tr>
<td>light dynamic 1</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="set-cp-offset-to-cp-percentage-between-two-control-points">Set CP offset to CP percentage between two control points</h3>

<table>
<thead>
<tr>
<th>Set CP offset to CP percentage between two control points</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_CPOffsetToPercentageBetweenCPs</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>153</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>input min</td>
<td>float</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>offset CP</td>
<td>integer</td>
</tr>
<tr>
<td>offset</td>
<td>vector</td>
</tr>
<tr>
<td>input bias</td>
<td>float</td>
</tr>
<tr>
<td>scale offset</td>
<td>boolean</td>
</tr>
<tr>
<td>end CP</td>
<td>integer</td>
</tr>
<tr>
<td>input CP</td>
<td>integer</td>
</tr>
<tr>
<td>ouput CP</td>
<td>integer</td>
</tr>
<tr>
<td>radial check</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="rotation-from-cp-forward-orientation">Rotation from CP forward orientation</h3>

<table>
<thead>
<tr>
<th>Rotation from CP forward orientation</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapCPOrientationToYaw</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>137</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>rot offset</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>spin strength</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="remap-cp-orientaton-to-rotations">Remap CP orientaton to rotations</h3>

<table>
<thead>
<tr>
<th>Remap CP orientaton to rotations</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapCPOrientationToRotations</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>116</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>Two New Options: <br><b>Use Quoternions Internally :</b><br> will use the Control points Matrix to extract Quoternion Rotations and apply that to the Orientation of the Particle. <br><br><b>Write Normal instead of Rotation :</b><br> is a sub section of Use Quaternion and will extract the CP Quoternion Fwd (X) Direction and map it to the Particle Normal. <br><br>While Off operator will work as before.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation</td>
<td>vector</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>use quat</td>
<td>boolean</td>
</tr>
<tr>
<td>write normal</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="lerp-endcap-vector">Lerp endcap vector</h3>

<table>
<thead>
<tr>
<th>Lerp endcap vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_LerpEndCapVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>109</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>lerp time</td>
<td>float</td>
</tr>
<tr>
<td>output</td>
<td>vector</td>
</tr>
</tbody>
</table><h3 id="normalize-vector">Normalize vector</h3>

<table>
<thead>
<tr>
<th>Normalize vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_NormalizeVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>98</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="remap-distance-between-two-control-points-to-scalar">Remap distance between two control points to scalar</h3>

<table>
<thead>
<tr>
<th>Remap distance between two control points to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_DistanceBetweenCPs</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>96</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>input min</td>
<td>float</td>
</tr>
<tr>
<td>end CP</td>
<td>integer</td>
</tr>
<tr>
<td>set method</td>
<td>integer</td>
</tr>
<tr>
<td>scale initial range</td>
<td>boolean</td>
</tr>
<tr>
<td>scale current</td>
<td>boolean</td>
</tr>
<tr>
<td>start CP</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="remap-distance-between-two-control-points-to-scalar-1">Remap distance between two control points to scalar</h3>

<table>
<thead>
<tr>
<th>Remap distance between two control points to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_DistanceBetweenCPsToCP</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>90</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>input min</td>
<td>float</td>
</tr>
<tr>
<td>end CP</td>
<td>integer</td>
</tr>
<tr>
<td>start CP</td>
<td>integer</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>output CP</td>
<td>integer</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>notes</td>
<td>string</td>
</tr>
</tbody>
</table><h3 id="remap-game-visibility-scalar">Remap game visibility scalar</h3>

<table>
<thead>
<tr>
<th>Remap game visibility scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapVisibilityScalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>88</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>radius scale</td>
<td>float</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>input min</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="movement-loop-inside-sphere">Movement loop inside sphere</h3>

<table>
<thead>
<tr>
<th>Movement loop inside sphere</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_MovementLoopInsideSphere</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>80</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>distance</td>
<td>float</td>
</tr>
<tr>
<td>scale</td>
<td>vector</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="remap-particle-count-on-endcap-scalar">Remap particle count on endcap scalar</h3>

<table>
<thead>
<tr>
<th>Remap particle count on endcap scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapParticleCountOnScalarEndCap</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>78</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>input max</td>
<td>integer</td>
</tr>
<tr>
<td>backwards</td>
<td>boolean</td>
</tr>
<tr>
<td>scale current</td>
<td>boolean</td>
</tr>
<tr>
<td>input min</td>
<td>integer</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>scale initial range</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="clamp-vector">Clamp vector</h3>

<table>
<thead>
<tr>
<th>Clamp vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_ClampVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>74</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Limits the specified vector’s value to a range between <b>output minimum</b> and <b>output maximum</b>.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>output max</td>
<td>vector</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>output min</td>
<td>vector</td>
</tr>
</tbody>
</table><h3 id="movement-match-particle-velocities">Movement match particle velocities</h3>

<table>
<thead>
<tr>
<th>Movement match particle velocities</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_VelocityMatchingForce</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>68</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>Forces particles to inherit the velocity of the first one emitted. Can copy the recorded value to a control point.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>spd scale</td>
<td>float</td>
</tr>
<tr>
<td>dir scale</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="restart-effect-after-duration">Restart effect after duration</h3>

<table>
<thead>
<tr>
<th>Restart effect after duration</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RestartAfterDuration</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>64</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>only children</td>
<td>boolean</td>
</tr>
<tr>
<td>duration max</td>
<td>float</td>
</tr>
<tr>
<td>duration min</td>
<td>float</td>
</tr>
<tr>
<td>child group ID</td>
<td>integer</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>CP field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="remap-game-visibility-of-cp-to-scalar">Remap game visibility of CP to scalar</h3>

<table>
<thead>
<tr>
<th>Remap game visibility of CP to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapCPVisibilityToScalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>64</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>control point</td>
<td>integer</td>
</tr>
<tr>
<td>radius</td>
<td>float</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="remap-difference-of-sequential-particle-vector-to-scalar">Remap difference of sequential particle vector to Scalar</h3>

<table>
<thead>
<tr>
<th>Remap difference of sequential particle vector to Scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_DifferencePreviousParticle</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>58</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>input min</td>
<td>float</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>set previous particle</td>
<td>boolean</td>
</tr>
<tr>
<td>scale initial range</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="remap-particle-count-to-scalar">Remap particle count to scalar</h3>

<table>
<thead>
<tr>
<th>Remap particle count to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapParticleCountToScalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>51</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>active range</td>
<td>boolean</td>
</tr>
<tr>
<td>input max</td>
<td>float (special)</td>
</tr>
<tr>
<td>output max</td>
<td>float (special)</td>
</tr>
<tr>
<td>output min</td>
<td>float (special)</td>
</tr>
<tr>
<td>input min</td>
<td>float (special)</td>
</tr>
<tr>
<td>scale initial range</td>
<td>boolean</td>
</tr>
<tr>
<td>set method</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="movement-maintain-offset">Movement maintain offset</h3>

<table>
<thead>
<tr>
<th>Movement maintain offset</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_MovementMaintainOffset</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>51</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>offset</td>
<td>vector</td>
</tr>
<tr>
<td>radius scale</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="set-cp-orientation-to-cp-direction">Set CP orientation to CP direction</h3>

<table>
<thead>
<tr>
<th>Set CP orientation to CP direction</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetCPOrientationToDirection</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>47</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>output control point</td>
<td>integer</td>
</tr>
<tr>
<td>input control point</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="cull-when-crossing-plane">Cull when crossing plane</h3>

<table>
<thead>
<tr>
<th>Cull when crossing plane</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_PlaneCull</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>46</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Instantly destroys particles when they pass the specified plane.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>plane control point</td>
<td>integer</td>
</tr>
<tr>
<td>plane offset</td>
<td>float</td>
</tr>
<tr>
<td>plane direction</td>
<td>vector</td>
</tr>
</tbody>
</table><h3 id="remap-percentage-between-two-control-points-to-vector">Remap percentage between two control points to vector</h3>

<table>
<thead>
<tr>
<th>Remap percentage between two control points to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_PercentageBetweenCPsVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>35</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>output max</td>
<td>vector</td>
</tr>
<tr>
<td>input min</td>
<td>float</td>
</tr>
<tr>
<td>output min</td>
<td>vector</td>
</tr>
<tr>
<td>start CP</td>
<td>integer</td>
</tr>
<tr>
<td>end CP</td>
<td>integer</td>
</tr>
<tr>
<td>active range</td>
<td>boolean</td>
</tr>
<tr>
<td>scale initial range</td>
<td>boolean</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>radial check</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="remap-scalar-once-timed">Remap scalar once timed</h3>

<table>
<thead>
<tr>
<th>Remap scalar once timed</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapScalarOnceTimed</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>33</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>input min</td>
<td>float</td>
</tr>
<tr>
<td>field input</td>
<td>integer</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>remap time</td>
<td>float</td>
</tr>
<tr>
<td>proportional</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="cycle-scalar">Cycle Scalar</h3>

<table>
<thead>
<tr>
<th>Cycle Scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_CycleScalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>33</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>dest field</td>
<td>integer</td>
</tr>
<tr>
<td>start value</td>
<td>float</td>
</tr>
<tr>
<td>end value</td>
<td>float</td>
</tr>
<tr>
<td>cycle time</td>
<td>float</td>
</tr>
<tr>
<td>synchronize particles</td>
<td>boolean</td>
</tr>
<tr>
<td>CP scale</td>
<td>integer</td>
</tr>
<tr>
<td>set method</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="lifespan-from-endcap-decay">Lifespan from endcap decay</h3>

<table>
<thead>
<tr>
<th>Lifespan from endcap decay</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_endcapdecay</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>31</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>
<h3 id="remap-vector-to-cp">Remap vector to CP</h3>

<table>
<thead>
<tr>
<th>Remap vector to CP</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapVectortoCP</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>29</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>out control point number</td>
<td>integer</td>
</tr>
<tr>
<td>field input</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="set-vec">Set Vec</h3>

<table>
<thead>
<tr>
<th>Set Vec</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetVec</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>27</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>input value</td>
<td>vector (special)</td>
</tr>
<tr>
<td>output field</td>
<td>integer</td>
</tr>
<tr>
<td>lerp</td>
<td>float (special)</td>
</tr>
</tbody>
</table><h3 id="lerp-initial-vector">Lerp initial vector</h3>

<table>
<thead>
<tr>
<th>Lerp initial vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_LerpVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>27</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>output</td>
<td>vector</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>scale initial range</td>
<td>boolean</td>
</tr>
<tr>
<td>start time</td>
<td>float</td>
</tr>
<tr>
<td>end time</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="set-cp-orientation-to-ground-normal">Set CP orientation to ground normal</h3>

<table>
<thead>
<tr>
<th>Set CP orientation to ground normal</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetCPOrientationToGroundNormal</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>21</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>interp rate</td>
<td>float</td>
</tr>
<tr>
<td>collision group name</td>
<td>string</td>
</tr>
<tr>
<td>max trace length</td>
<td>float</td>
</tr>
<tr>
<td>output CP</td>
<td>integer</td>
</tr>
<tr>
<td>tolerance</td>
<td>float</td>
</tr>
<tr>
<td>include water</td>
<td>boolean</td>
</tr>
<tr>
<td>trace offset</td>
<td>float</td>
</tr>
<tr>
<td>input CP</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="pin-particle-to-control-point">Pin Particle to control point</h3>

<table>
<thead>
<tr>
<th>Pin Particle to control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_PinParticleToCP</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>20</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="remap-dot-product-to-scalar">Remap dot product to scalar</h3>

<table>
<thead>
<tr>
<th>Remap dot product to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapDotProductToScalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>19</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>input CP2</td>
<td>integer</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="movement-lock-to-saved-position-along-path-1">Movement lock to saved position along path</h3>

<table>
<thead>
<tr>
<th>Movement lock to saved position along path</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_LockToSavedSequentialPathV2</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>19</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>CP pairs</td>
<td>boolean</td>
</tr>
<tr>
<td>path params</td>
<td>path params (special)</td>
</tr>
</tbody>
</table><h3 id="lifespan-maintain-count-decay">Lifespan maintain count decay</h3>

<table>
<thead>
<tr>
<th>Lifespan maintain count decay</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_DecayMaintainCount</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>18</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>particles to maintain</td>
<td>integer</td>
</tr>
<tr>
<td>scale control point</td>
<td>integer</td>
</tr>
<tr>
<td>decay delay</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="reinitalize-on-endcap-scalar-random">Reinitalize on endcap scalar random</h3>

<table>
<thead>
<tr>
<th>Reinitalize on endcap scalar random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_ReinitializeScalarEndCap</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>17</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="remap-cp-velocity-to-vector">Remap CP velocity to vector</h3>

<table>
<thead>
<tr>
<th>Remap CP velocity to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapCPVelocityToVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>7</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>normalize</td>
<td>boolean</td>
</tr>
<tr>
<td>control point</td>
<td>integer</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="set-vector-from-control-point">Set vector from control point</h3>

<table>
<thead>
<tr>
<th>Set vector from control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetCPtoVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>6</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>CP input</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="movement-lerp-to-initial-position-relative-to-cp">Movement Lerp to Initial Position relative to CP</h3>

<table>
<thead>
<tr>
<th>Movement Lerp to Initial Position relative to CP</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_LerpToInitialPosition</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>6</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>This operator moves particles back to their starting point relative to a control point.  It interpolates them, so the strength of the move (and inversely, how much other forces can move them) can be modulated by lifespan/curve/random range/whatever.  For example they can fly off into space, then reassemble themselves over time into their original pattern.  The original position can be anything – a position within sphere, grid, ring, snapshot, etc.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
<th>Tooltip</th>
</tr>
</thead>
<tbody>
<tr>
<td>scale</td>
<td>float (special)</td>
<td></td>
<td></td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
<td>This operator will interpolate particles into the same position relative to a control point that they were initialized in.The interpolation factor will determine how fast/strong the effect is.<b>This field is the control point that is specified for the relative position.</b></td>
<td>Initial Position Reference CP</td>
</tr>
</tbody>
</table><h3 id="calculate-vector-attribute">Calculate vector attribute</h3>

<table>
<thead>
<tr>
<th>Calculate vector attribute</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_CalculateVectorAttribute</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>6</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>This lets you specify up to 2 vector attributes (with weights), and up to two control points (with offsets and weights), plus an initial value and a final scale (both vectors). It then does this calculation:<blockquote>Output_attribute = final scale * ( start value + inputscale1<em>inputfield1 + inputscale2</em>inputfield2 + controlpoint1*controlpointscale1 + controlpoint2 * controlpoint2scale);</blockquote>     (Then, If the output attribute is “particle normal”, it will normalize it).<br><br>This has many uses, and can mix attributes together, normalize attributes, scale them, offset them, etc.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>control point input 1</td>
<td>control point</td>
</tr>
</tbody>
</table><h3 id="remap-on-endcap-scalar">Remap on endcap scalar</h3>

<table>
<thead>
<tr>
<th>Remap on endcap scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapScalarEndCap</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>5</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>field input</td>
<td>integer</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>input min</td>
<td>float</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="remap-distance-to-line-between-2-control-points-to-vector">Remap distance to line between 2 control points to vector</h3>

<table>
<thead>
<tr>
<th>Remap distance to line between 2 control points to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapDistanceToLineSegmentToVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>5</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>min output value</td>
<td>vector</td>
</tr>
<tr>
<td>max output value</td>
<td>vector</td>
</tr>
<tr>
<td>max input value</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="remap-control-point-orientaton-to-rotation">Remap control point orientaton to rotation</h3>

<table>
<thead>
<tr>
<th>Remap control point orientaton to rotation</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapControlPointOrientationToRotation</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>4</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>This operator is intended for sprite based renderers.  It will take the specified Control Points orientation along an axis and set the specified sprite rotation to the same rotation.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
<th>Tooltip</th>
</tr>
</thead>
<tbody>
<tr>
<td>control point number</td>
<td>integer</td>
<td>This operator is intended for sprite based renderers. It will take the specified Control Points orientation along an axis and set the specified sprite rotation to the same rotation. This field is for the referenced control point.</td>
<td>Control Point to reference for rotation</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
<td>This operator is intended for sprite based renderers. It will take the specified Control Points orientation along an axis and set the specified sprite rotation to the same rotation. This field is for the rotation you wish to set on the sprites.</td>
<td>Rotation value to change on particle</td>
</tr>
</tbody>
</table><h3 id="remap-distance-to-line-between-2-control-points-to-scalar">Remap distance to line between 2 control points to scalar</h3>

<table>
<thead>
<tr>
<th>Remap distance to line between 2 control points to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapDistanceToLineSegmentToScalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>3</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>min output value</td>
<td>float</td>
</tr>
<tr>
<td>max input value</td>
<td>float</td>
</tr>
<tr>
<td>max output value</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="remap-percentage-between-two-cps-to-lerp-cps-to-scalar">Remap percentage between two cps to lerp CPs to scalar</h3>

<table>
<thead>
<tr>
<th>Remap percentage between two cps to lerp CPs to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_PercentageBetweenCPLerpCPs</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>radial check</td>
<td>boolean</td>
</tr>
<tr>
<td>scale initial range</td>
<td>boolean</td>
</tr>
<tr>
<td>output end CP</td>
<td>integer</td>
</tr>
<tr>
<td>output start field</td>
<td>integer</td>
</tr>
<tr>
<td>output start CP</td>
<td>integer</td>
</tr>
<tr>
<td>end CP</td>
<td>integer</td>
</tr>
<tr>
<td>start CP</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="remap-control-point-to-velocity">Remap control point to velocity</h3>

<table>
<thead>
<tr>
<th>Remap control point to velocity</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapCPtoVelocity</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>CP input</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="point-vector-at-next-particle-position">Point vector at next particle position</h3>

<table>
<thead>
<tr>
<th>Point vector at next particle position</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_PointVectorAtNextParticle</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody></tbody>
</table><h2 id="init">Init</h2>
<h3 id="lifetime-random">Lifetime random</h3>

<table>
<thead>
<tr>
<th>Lifetime random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RandomLifeTime</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>33523</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Defines the lifetime of each particle in seconds, chosen randomly, between <b>lifetime_min</b> and <b>lifetime_max</b>.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>lifetime max</td>
<td>float</td>
</tr>
<tr>
<td>lifetime min</td>
<td>float</td>
</tr>
<tr>
<td>lifetime rand exponent</td>
<td>float</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
</tr>
<tr>
<td>notes</td>
<td>string</td>
</tr>
</tbody>
</table><h3 id="radius-random">Radius Random</h3>

<table>
<thead>
<tr>
<th>Radius Random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RandomRadius</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>29028</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Initializes each particle with a random radius within the specified range.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>radius min</td>
<td>float</td>
</tr>
<tr>
<td>radius max</td>
<td>float</td>
</tr>
<tr>
<td>radius rand exponent</td>
<td>float</td>
</tr>
<tr>
<td>notes</td>
<td>string</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="rotation-random">Rotation random</h3>

<table>
<thead>
<tr>
<th>Rotation random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RandomRotation</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>24297</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Randomly picks an initial rotation value for each particle within the specified range. The axis is chosen through the <b>rotation field</b> property.</p><p><b><i>NOTE</i></b>: The properties <b>yaw_offset_min</b> and <b>yaw_offset_max</b> are mis-named at the time of this writing. They should instead read “rotation min” and “rotation max” - these define the range.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>degrees max</td>
<td>float</td>
</tr>
<tr>
<td>randomly flip direction</td>
<td>boolean</td>
</tr>
<tr>
<td>degrees min</td>
<td>float</td>
</tr>
<tr>
<td>degrees</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="color-random">Color Random</h3>

<table>
<thead>
<tr>
<th>Color Random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RandomColor</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>23577</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Initializes each particle with a random color within the specified range.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>color min</td>
<td>vector</td>
</tr>
<tr>
<td>color max</td>
<td>vector</td>
</tr>
<tr>
<td>tint perc</td>
<td>float</td>
</tr>
<tr>
<td>tint max</td>
<td>vector</td>
</tr>
<tr>
<td>tint min</td>
<td>vector</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
</tr>
<tr>
<td>tint blend mode</td>
<td>integer</td>
</tr>
<tr>
<td>tint CP</td>
<td>integer</td>
</tr>
<tr>
<td>update threshold</td>
<td>float</td>
</tr>
<tr>
<td>light amplification</td>
<td>float</td>
</tr>
<tr>
<td>notes</td>
<td>string</td>
</tr>
</tbody>
</table><h3 id="position-within-sphere-random">Position within sphere random</h3>

<table>
<thead>
<tr>
<th>Position within sphere random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_CreateWithinSphere</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>22661</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Randomly spawns a particle within a sphere that’s centered on the specified control point.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>radius max</td>
<td>float</td>
<td>Maximum distance to spawn from the center of the sphere.</td>
</tr>
<tr>
<td>speed min</td>
<td>float</td>
<td>Minimum initial speed of the particle emitted outward from the sphere.</td>
</tr>
<tr>
<td>speed max</td>
<td>float</td>
<td>Maximum initial speed of the particle emitted outward from the sphere.</td>
</tr>
<tr>
<td>distance bias</td>
<td>vector</td>
<td>A bias to the distribution of particles in the system in X Y Z relative to each axis. 1 1 0 will create particles only in the X Y plane, while 1 1 10 will create roughly 10 times as many particles near the top and bottom of the sphere as on the X Y parts. Useful for creating discs, rings, and polar effects.</td>
</tr>
<tr>
<td>distance bias abs</td>
<td>vector</td>
<td>Setting any axis to one will eliminate particles from one hemisphere of the distribution. Can be used to create hemispheres, quarter spheres, etc. Use wil distance bias to alter the effect. Use negative values in distance bias to flip the hemisphere from one side to the other.</td>
</tr>
<tr>
<td>radius min</td>
<td>float</td>
<td>Minimum distance to spawn from the center of the sphere.</td>
</tr>
<tr>
<td>local coordinate system speed max</td>
<td>vector</td>
<td>Local space maximum initial speed of the particle in x y z.</td>
</tr>
<tr>
<td>local coordinate system speed min</td>
<td>vector</td>
<td>Local space minimum initial speed of the particle in x y z.</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
<td>This operator will interpolate particles into the same position relative to a control point that they were initialized in.The interpolation factor will determine how fast/strong the effect is.<b>This field is the control point that is specified for the relative position.</b></td>
</tr>
<tr>
<td>local coords</td>
<td>boolean</td>
<td>This bool (0/1) sets where to use world or local (emitter) space to do the offset.</td>
</tr>
<tr>
<td>scale CP</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>end CP growth time</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>speed rand exp</td>
<td>float</td>
<td>The exponent which determines the biasing of particles towards one end or the other of the random range.</td>
</tr>
<tr>
<td>use highest end CP</td>
<td>boolean</td>
<td></td>
</tr>
</tbody>
</table><h3 id="alpha-random">Alpha Random</h3>

<table>
<thead>
<tr>
<th>Alpha Random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RandomAlpha</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>18841</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Particles will be created with a random alpha value within the specified range (0-255).</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>alpha min</td>
<td>integer</td>
</tr>
<tr>
<td>alpha max</td>
<td>integer</td>
</tr>
<tr>
<td>alpha rand exponent</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="position-modify-offset-random">Position modify offset random</h3>

<table>
<thead>
<tr>
<th>Position modify offset random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_PositionOffset</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>16846</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>Moves the initial position of a particle in world or local space relative to its emission point.<p>Generally used in combination with other Position initializers. For example, it can be used to emit particles along a line while still using parts of a sphere emitter.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>offset max</td>
<td>vector</td>
<td></td>
</tr>
<tr>
<td>offset min</td>
<td>vector</td>
<td></td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
<td>This operator will interpolate particles into the same position relative to a control point that they were initialized in.The interpolation factor will determine how fast/strong the effect is.<b>This field is the control point that is specified for the relative position.</b></td>
</tr>
<tr>
<td>local coords</td>
<td>boolean</td>
<td>This bool (0/1) sets where to use world or local (emitter) space to do the offset.</td>
</tr>
<tr>
<td>proportional</td>
<td>boolean</td>
<td>This bool (0/1) sets whether to treat the offset values as an amount relative to the particle’s radius. For example, if the offset is set to 0 0 1, and two particles have a radii of 32 and 64, they’d be moved vertically 32 and 64 units respectively.</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
<td></td>
</tr>
</tbody>
</table><h3 id="sequence-random">Sequence Random</h3>

<table>
<thead>
<tr>
<th>Sequence Random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RandomSequence</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>12637</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>When using a multi-frame texture, this allows particles to randomly start at a minimum and maximum supplied frame.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>sequence max</td>
<td>integer</td>
</tr>
<tr>
<td>sequence min</td>
<td>integer</td>
</tr>
<tr>
<td>shuffle</td>
<td>boolean</td>
</tr>
<tr>
<td>linear</td>
<td>boolean</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="velocity-noise">Velocity noise</h3>

<table>
<thead>
<tr>
<th>Velocity noise</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_InitialVelocityNoise</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>10100</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>Allows particle velocity to be initialized to a select range via a noise function. The noise function is mapped based on both time and space, each with their own coordinate scales and offsets. This creates a range of results that are non-random but vary based on creation time and position.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>output min</td>
<td>vector</td>
</tr>
<tr>
<td>output max</td>
<td>vector</td>
</tr>
<tr>
<td>noise scale</td>
<td>float</td>
</tr>
<tr>
<td>noise scale loc</td>
<td>float</td>
</tr>
<tr>
<td>use local space</td>
<td>boolean</td>
</tr>
<tr>
<td>ignore dt</td>
<td>boolean</td>
</tr>
<tr>
<td>offset</td>
<td>float</td>
</tr>
<tr>
<td>offset loc</td>
<td>vector</td>
</tr>
<tr>
<td>abs val inv</td>
<td>vector</td>
</tr>
<tr>
<td>abs val</td>
<td>vector</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="rotation-yaw-flip-random">Rotation yaw flip random</h3>

<table>
<thead>
<tr>
<th>Rotation yaw flip random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RandomYawFlip</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>8320</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>percent</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="remap-particle-count-to-scalar-1">Remap particle count to scalar</h3>

<table>
<thead>
<tr>
<th>Remap particle count to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RemapParticleCountToScalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>6822</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>input max</td>
<td>integer</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>scale initial range</td>
<td>boolean</td>
</tr>
<tr>
<td>active range</td>
<td>boolean</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>input min</td>
<td>integer</td>
</tr>
<tr>
<td>invert</td>
<td>boolean</td>
</tr>
<tr>
<td>set method</td>
<td>integer</td>
</tr>
<tr>
<td>scale control point</td>
<td>integer</td>
</tr>
<tr>
<td>remap bias</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="rotation-speed-random">Rotation speed random</h3>

<table>
<thead>
<tr>
<th>Rotation speed random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RandomRotationSpeed</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>5335</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>degrees max</td>
<td>float</td>
</tr>
<tr>
<td>degrees min</td>
<td>float</td>
</tr>
<tr>
<td>randomly flip direction</td>
<td>boolean</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>degrees</td>
<td>float</td>
</tr>
<tr>
<td>rotation rand exponent</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="position-along-ring">Position along ring</h3>

<table>
<thead>
<tr>
<th>Position along ring</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RingWave</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>5137</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Initializes particle positions along a whole or partial ring.</p><p>Like “Position Within Sphere Random”, this initializer has additional functionality that can impart radial force to particles via <b>min initial speed</b> and <b>max initial speed</b>.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>initial speed max</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>initial speed min</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>initial radius</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>particles per orbit</td>
<td>float</td>
<td>This along with turning on “even distribution” will evenly space the particles around the ring using X particles</td>
</tr>
<tr>
<td>even distribution</td>
<td>boolean</td>
<td>Enabling even distribution will evenly space the particles around the ring.</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
<td>This operator will interpolate particles into the same position relative to a control point that they were initialized in.The interpolation factor will determine how fast/strong the effect is.<b>This field is the control point that is specified for the relative position.</b></td>
</tr>
<tr>
<td>override CP</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>thickness</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>yaw</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>pitch</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>XY velocity only</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>roll</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>override CP2</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
<td></td>
</tr>
</tbody>
</table><h3 id="remap-scalar-1">Remap scalar</h3>

<table>
<thead>
<tr>
<th>Remap scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RemapScalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>3301</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Remaps any exposed scalar’s initial value to any other scalar.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>scale initial range</td>
<td>boolean</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>field input</td>
<td>integer</td>
</tr>
<tr>
<td>active range</td>
<td>boolean</td>
</tr>
<tr>
<td>input min</td>
<td>float</td>
</tr>
<tr>
<td>end time</td>
<td>float</td>
</tr>
<tr>
<td>start time</td>
<td>float</td>
</tr>
<tr>
<td>set method</td>
<td>integer</td>
</tr>
<tr>
<td>remap bias</td>
<td>float</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="trail-length-random">Trail length random</h3>

<table>
<thead>
<tr>
<th>Trail length random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RandomTrailLength</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>3183</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>min length</td>
<td>float</td>
</tr>
<tr>
<td>max length</td>
<td>float</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
</tr>
<tr>
<td>length rand exponent</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="remap-control-point-to-scalar-1">Remap control point to scalar</h3>

<table>
<thead>
<tr>
<th>Remap control point to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RemapCPtoScalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2740</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>CP input</td>
<td>integer</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>scale initial range</td>
<td>boolean</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>field</td>
<td>integer</td>
</tr>
<tr>
<td>input min</td>
<td>float</td>
</tr>
<tr>
<td>set method</td>
<td>integer</td>
</tr>
<tr>
<td>notes</td>
<td>string</td>
</tr>
<tr>
<td>end time</td>
<td>float</td>
</tr>
<tr>
<td>start time</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="position-from-parent-particles">Position from parent particles</h3>

<table>
<thead>
<tr>
<th>Position from parent particles</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_CreateFromParentParticles</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2499</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>increment</td>
<td>float</td>
</tr>
<tr>
<td>random distribution</td>
<td>boolean</td>
</tr>
<tr>
<td>sub frame</td>
<td>boolean</td>
</tr>
<tr>
<td>velocity scale</td>
<td>float</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
</tr>
<tr>
<td>random seed</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="position-modify-place-on-ground">Position modify place on ground</h3>

<table>
<thead>
<tr>
<th>Position modify place on ground</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_PositionPlaceOnGround</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2262</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>“Snaps” each particle to the ground (or a specified offset above the ground.)</p><p>Note that this operator only searches for ground BELOW its current position - if the particle is already below the ground, it won’t snap to the ground above. If there’s any doubt, simply add a Position Modify Offset Random initializer above this one in the initializer stack.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>offset</td>
<td>float</td>
</tr>
<tr>
<td>collision group name</td>
<td>string</td>
</tr>
<tr>
<td>include water</td>
<td>boolean</td>
</tr>
<tr>
<td>max trace length</td>
<td>float</td>
</tr>
<tr>
<td>set normal</td>
<td>boolean</td>
</tr>
<tr>
<td>kill</td>
<td>boolean</td>
</tr>
<tr>
<td>set PXYZ only</td>
<td>boolean</td>
</tr>
<tr>
<td>offset by radius factor</td>
<td>float</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="position-skin-to-bones-from-cp-snapshot">Position skin to bones from CP snapshot</h3>

<table>
<thead>
<tr>
<th>Position skin to bones from CP snapshot</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_InitSkinnedPositionFromCPSnapshot</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1983</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>snapshot control point number</td>
<td>integer</td>
</tr>
<tr>
<td>rigid</td>
<td>boolean</td>
</tr>
<tr>
<td>random</td>
<td>boolean</td>
</tr>
<tr>
<td>set normal</td>
<td>boolean</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>bone velocity</td>
<td>float</td>
</tr>
<tr>
<td>bone velocity max</td>
<td>float</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
</tr>
<tr>
<td>min normal velocity</td>
<td>float</td>
</tr>
<tr>
<td>max normal velocity</td>
<td>float</td>
</tr>
<tr>
<td>ignore dt</td>
<td>boolean</td>
</tr>
<tr>
<td>random seed</td>
<td>integer</td>
</tr>
<tr>
<td>snap shot start point</td>
<td>integer</td>
</tr>
<tr>
<td>increment</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="rotation-yaw-random">Rotation yaw random</h3>

<table>
<thead>
<tr>
<th>Rotation yaw random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RandomYaw</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1955</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>degrees max</td>
<td>float</td>
</tr>
<tr>
<td>degrees min</td>
<td>float</td>
</tr>
<tr>
<td>degrees</td>
<td>float</td>
</tr>
<tr>
<td>randomly flip direction</td>
<td>boolean</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
</tr>
<tr>
<td>rotation rand exponent</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="remap-noise-to-scalar">Remap noise to scalar</h3>

<table>
<thead>
<tr>
<th>Remap noise to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_CreationNoise</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1937</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>Allows any scalar parameter to be initialized to a select range via a noise function. The noise function is mapped based on both time and space, each with their own coordinate scales and offsets. This creates a range of results that are non-random but vary based on creation time and position.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>noise scale</td>
<td>float</td>
<td>This sets the scale of the time part of the noise function - based on particle spawn time. Larger numbers will appear increasingly random, while very small numbers will map to a similar area of the noise and look very similar.</td>
</tr>
<tr>
<td>noise scale loc</td>
<td>float</td>
<td>This sets the scale of the spatial part of the noise function - based on particle spawn location. Larger numbers will appear increasingly random, while very small numbers will map to a similar area of the noise and look very similar. Time noise is added to spatial noise, so set one or the other to zero in order to receive no effect from that portion of the function.</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
<td>This operator is intended for sprite based renderers. It will take the specified Control Points orientation along an axis and set the specified sprite rotation to the same rotation. This field is for the rotation you wish to set on the sprites.</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>abs val</td>
<td>boolean</td>
<td>Noise returns -1 to 1 which is mapped to the output range. Using absolute value bool (0/1) , the output can have sudden shifts in direction as the number approaches zero and then bounces back into positives instead of going into negatives.</td>
</tr>
<tr>
<td>offset</td>
<td>float</td>
<td>This sets the offset on the noise function to draw from. Two initial scalar noise functions set to different outputs (say alpha and radius) set to the same coordinate scales will behave the same. Offsets allow for the same scale mapping, but at a different part of the noise. So for example all small radius particles may have a high alpha rather than a low one if the offset is used.</td>
</tr>
<tr>
<td>abs val inv</td>
<td>boolean</td>
<td>Essentially flips the curve created by using the absolute value flag. So instead of getting sharp valleys, you get sharp peaks. The math is 1 minus the absolute value of the noise.</td>
</tr>
<tr>
<td>world time scale</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>offset loc</td>
<td>vector</td>
<td>This sets the offset on the noise function to draw from. Two initial scalar noise functions set to different outputs (say alpha and radius) set to the same coordinate scales will behave the same. Offsets allow for the same scale mapping, but at a different part of the noise. So for example all small radius particles may have a high alpha rather than a low one if the offset is used.</td>
</tr>
</tbody>
</table><h3 id="inherit-attribute-from-parent-particle-2">Inherit attribute from parent particle</h3>

<table>
<thead>
<tr>
<th>Inherit attribute from parent particle</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_InheritFromParentParticles</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1738</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Assigns a parent particle’s attribute to each particle’s initial value for that attribute.</p><p>This differs from the operator “Inherit Attribute from Parent Particle” in that it runs only once, on particle initialization.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>scale</td>
<td>float</td>
</tr>
<tr>
<td>random distribution</td>
<td>boolean</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
</tr>
<tr>
<td>increment</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="position-modify-warp-random">Position modify warp random</h3>

<table>
<thead>
<tr>
<th>Position modify warp random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_PositionWarp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1671</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Warps the initial position of a particle in world or local space relative to its emission point. Can be used to stretch initial emission shapes. A sphere can be stretched into an ovoid, or smashed.</p><p>Useful in addition to sphere emissions distance bias and absolute value to create squashed domes, rings (the elongated ring seen in Portal), etc. Warped particles’ initial speed is also warped by the corresponding amount. So particles that are stretched will have a higher initial velocity, while those that are squashed will have lower.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>warp min</td>
<td>vector</td>
<td></td>
</tr>
<tr>
<td>warp max</td>
<td>vector</td>
<td></td>
</tr>
<tr>
<td>warp time</td>
<td>float</td>
<td>Treats the min/max as start and end sizes for a warp that takes place over the specified time. So the emission placement of each new particle will be warped over time.</td>
</tr>
<tr>
<td>use count</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
<td>This operator will interpolate particles into the same position relative to a control point that they were initialized in.The interpolation factor will determine how fast/strong the effect is.<b>This field is the control point that is specified for the relative position.</b></td>
</tr>
<tr>
<td>scale control point number</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>warp start time</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>invert warp</td>
<td>boolean</td>
<td>In the case of a warp transition, it will make it run backwards (max to min).</td>
</tr>
<tr>
<td>radius component</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>prev pos scale</td>
<td>float</td>
<td></td>
</tr>
</tbody>
</table><h3 id="velocity-random">Velocity random</h3>

<table>
<thead>
<tr>
<th>Velocity random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_VelocityRandom</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1504</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>local coordinate system speed min</td>
<td>vector</td>
</tr>
<tr>
<td>local coordinate system speed max</td>
<td>vector</td>
</tr>
<tr>
<td>speed max</td>
<td>float</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>speed min</td>
<td>float</td>
</tr>
<tr>
<td>ignore DT</td>
<td>boolean</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="position-along-path-sequential">Position along path sequential</h3>

<table>
<thead>
<tr>
<th>Position along path sequential</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_CreateSequentialPath</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1480</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Initializes particle positions sequentially along a line between two control points.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>num to assign</td>
<td>float</td>
</tr>
<tr>
<td>path params</td>
<td>path params (special)</td>
</tr>
<tr>
<td>loop</td>
<td>boolean</td>
</tr>
<tr>
<td>CP pairs</td>
<td>boolean</td>
</tr>
<tr>
<td>max distance</td>
<td>float</td>
</tr>
<tr>
<td>save offset</td>
<td>boolean</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="remap-control-point-to-vector-1">Remap control point to vector</h3>

<table>
<thead>
<tr>
<th>Remap control point to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RemapCPtoVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1354</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>input max</td>
<td>vector</td>
</tr>
<tr>
<td>output max</td>
<td>vector</td>
</tr>
<tr>
<td>CP input</td>
<td>integer</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>scale initial range</td>
<td>boolean</td>
</tr>
<tr>
<td>output min</td>
<td>vector</td>
</tr>
<tr>
<td>input min</td>
<td>vector</td>
</tr>
<tr>
<td>notes</td>
<td>string</td>
</tr>
<tr>
<td>remap bias</td>
<td>float</td>
</tr>
<tr>
<td>set method</td>
<td>integer</td>
</tr>
<tr>
<td>offset</td>
<td>boolean</td>
</tr>
<tr>
<td>local space CP</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="scalar-random">Scalar random</h3>

<table>
<thead>
<tr>
<th>Scalar random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RandomScalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1144</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Allows any exposed scalar (such as radius, alpha, lifetime, etc.) to be initialized with a random value within the specified range.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>min</td>
<td>float</td>
</tr>
<tr>
<td>max</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>exponent</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="init-from-cp-snapshot">Init from CP snapshot</h3>

<table>
<thead>
<tr>
<th>Init from CP snapshot</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_InitFromCPSnapshot</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1082</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>attribute to read</td>
<td>integer</td>
</tr>
<tr>
<td>attribute to write</td>
<td>integer</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>local space CP</td>
<td>integer</td>
</tr>
<tr>
<td>reverse</td>
<td>boolean</td>
</tr>
<tr>
<td>random</td>
<td>boolean</td>
</tr>
<tr>
<td>local space angles</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="normal-align-to-cp">Normal align to CP</h3>

<table>
<thead>
<tr>
<th>Normal align to CP</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_NormalAlignToCP</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1057</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="sequence-two-random">Sequence two random</h3>

<table>
<thead>
<tr>
<th>Sequence two random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RandomSecondSequence</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>690</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>sequence max</td>
<td>integer</td>
</tr>
<tr>
<td>sequence min</td>
<td>integer</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="velocity-inherit-from-control-point">Velocity inherit from control point</h3>

<table>
<thead>
<tr>
<th>Velocity inherit from control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_InheritVelocity</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>676</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>velocity scale</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="offset-vector-to-vector">Offset vector to vector</h3>

<table>
<thead>
<tr>
<th>Offset vector to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_OffsetVectorToVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>658</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>output min</td>
<td>vector</td>
</tr>
<tr>
<td>output max</td>
<td>vector</td>
</tr>
<tr>
<td>field input</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="remap-initial-distance-to-control-point-to-scalar">Remap initial distance to control point to scalar</h3>

<table>
<thead>
<tr>
<th>Remap initial distance to control point to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_DistanceToCPInit</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>655</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>input min</td>
<td>float</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>start CP</td>
<td>integer</td>
</tr>
<tr>
<td>scale initial range</td>
<td>boolean</td>
</tr>
<tr>
<td>active range</td>
<td>boolean</td>
</tr>
<tr>
<td>set method</td>
<td>integer</td>
</tr>
<tr>
<td>distance scale</td>
<td>vector</td>
</tr>
</tbody>
</table><h3 id="position-along-epitrochoid">Position along epitrochoid</h3>

<table>
<thead>
<tr>
<th>Position along epitrochoid</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_CreateInEpitrochoid</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>571</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Initializes particle positions within an <a href="https://en.wikipedia.org/wiki/Epitrochoid">epitrochoid</a>.</p><p>Notably, this position initializer can be used to modify another position initializer if <b>offset from existing position</b> is checked. With the right combination of position initializers and epitrochoid settings, you can achieve positional noise with more coherence than simple random ranges offer.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>radius 1</td>
<td>float</td>
</tr>
<tr>
<td>offset</td>
<td>float</td>
</tr>
<tr>
<td>particle density</td>
<td>float</td>
</tr>
<tr>
<td>use count</td>
<td>boolean</td>
</tr>
<tr>
<td>use local coords</td>
<td>boolean</td>
</tr>
<tr>
<td>component 2</td>
<td>integer</td>
</tr>
<tr>
<td>offset existing pos</td>
<td>boolean</td>
</tr>
<tr>
<td>component 1</td>
<td>integer</td>
</tr>
<tr>
<td>radius 2</td>
<td>float</td>
</tr>
<tr>
<td>scale CP</td>
<td>integer</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="init-from-killed-parent-particle">Init from killed parent particle</h3>

<table>
<thead>
<tr>
<th>Init from killed parent particle</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_InitFromParentKilled</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>561</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>attribute to copy</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="normal-lock-to-control-point">Normal lock to control point</h3>

<table>
<thead>
<tr>
<th>Normal lock to control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_NormalLock</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>505</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="remap-cp-orientation-to-rotation">Remap CP orientation to rotation</h3>

<table>
<thead>
<tr>
<th>Remap CP orientation to rotation</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RemapInitialCPDirectionToRotation</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>413</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>This operator is intended for sprite based renderers.  It will take the specified Control Points orientation along an axis and set the specified sprite rotation to the same rotation.</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>offset of rotation</td>
<td>float</td>
</tr>
<tr>
<td>scale</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="position-within-box-random">Position within box random</h3>

<table>
<thead>
<tr>
<th>Position within box random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_CreateWithinBox</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>382</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Randomly spawns a particle within the specified volume.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>min</td>
<td>vector</td>
</tr>
<tr>
<td>max</td>
<td>vector</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>use local space</td>
<td>boolean</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="normal-modify-offset-random">Normal modify offset random</h3>

<table>
<thead>
<tr>
<th>Normal modify offset random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_NormalOffset</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>361</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>offset min</td>
<td>vector</td>
</tr>
<tr>
<td>offset max</td>
<td>vector</td>
</tr>
<tr>
<td>normalize</td>
<td>boolean</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>local coords</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="lifetime-from-sequence">Lifetime from sequence</h3>

<table>
<thead>
<tr>
<th>Lifetime from sequence</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_SequenceLifeTime</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>338</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Sets a particle’s lifespan based on the animation length of the sequence based at the given framerate. Used when a single particle type consists of many sequences with varying sequence lengths (some have 10 frames, others 60, but all must act appropriately without slow framerate, etc.)</p><p><i>Note:</i> If the ‘use animation rate as FPS’ flag of Render_Animated_Sprites has the same FPS settings, a particle will map it lifespan and animation together perfectly.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>framerate</td>
<td>float</td>
<td>Sets the desired FPS for the animation. This is mapped to lifespan according to the number of frames in the sequence the particle receives via a <b>sequence_random</b> or other sequence-defining initializer.</td>
</tr>
</tbody>
</table><h3 id="remap-initial-direction-to-cp-to-vector">Remap initial direction to CP to vector</h3>

<table>
<thead>
<tr>
<th>Remap initial direction to CP to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RemapInitialDirectionToCPToVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>333</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>normalize</td>
<td>boolean</td>
</tr>
<tr>
<td>offset axis</td>
<td>vector</td>
</tr>
<tr>
<td>scale</td>
<td>float</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>offset of rotation</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="init-float">Init Float</h3>

<table>
<thead>
<tr>
<th>Init Float</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_InitFloat</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>323</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>output field</td>
<td>integer</td>
</tr>
<tr>
<td>input value</td>
<td>float (special)</td>
</tr>
<tr>
<td>set method</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="velocity-set-from-control-point">Velocity set from control point</h3>

<table>
<thead>
<tr>
<th>Velocity set from control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_VelocityFromCP</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>298</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>control point</td>
<td>integer</td>
</tr>
<tr>
<td>control point compare</td>
<td>integer</td>
</tr>
<tr>
<td>velocity scale</td>
<td>float</td>
</tr>
<tr>
<td>direction only</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="rotation-spin-yaw">Rotation spin yaw</h3>

<table>
<thead>
<tr>
<th>Rotation spin yaw</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SpinYaw</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>292</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Rotates each particle along the “yaw” axis.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>spin rate degrees</td>
<td>integer</td>
</tr>
<tr>
<td>spin rate min degrees</td>
<td>integer</td>
</tr>
<tr>
<td>spin rate stop time</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="vector-component-random">Vector component random</h3>

<table>
<thead>
<tr>
<th>Vector component random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RandomVectorComponent</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>243</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>min</td>
<td>float</td>
</tr>
<tr>
<td>max</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>control point axis</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="rotation-orient-relative-to-cp-1">Rotation orient relative to CP</h3>

<table>
<thead>
<tr>
<th>Rotation orient relative to CP</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_Orient2DRelToCP</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>243</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rot offset</td>
<td>float</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="init-status-effect">Init Status Effect</h3>

<table>
<thead>
<tr>
<th>Init Status Effect</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_StatusEffect</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>193</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>ambient scale</td>
<td>float</td>
</tr>
<tr>
<td>rim light scale</td>
<td>float</td>
</tr>
<tr>
<td>specular scale</td>
<td>float</td>
</tr>
<tr>
<td>specular exponent</td>
<td>float</td>
</tr>
<tr>
<td>specular exponent blend to full</td>
<td>float</td>
</tr>
<tr>
<td>specular blend to full</td>
<td>float</td>
</tr>
<tr>
<td>color</td>
<td>vector</td>
</tr>
<tr>
<td>light color</td>
<td>vector</td>
</tr>
<tr>
<td>detail 2 combo</td>
<td>integer</td>
</tr>
<tr>
<td>color warp intensity</td>
<td>float</td>
</tr>
<tr>
<td>reflections tint by base blend to none</td>
<td>float</td>
</tr>
<tr>
<td>metalness blend to full</td>
<td>float</td>
</tr>
<tr>
<td>detail 2 scale</td>
<td>float</td>
</tr>
<tr>
<td>detail 2 blend factor</td>
<td>float</td>
</tr>
<tr>
<td>env map intensity</td>
<td>float</td>
</tr>
<tr>
<td>diffuse warp blend to full</td>
<td>float</td>
</tr>
<tr>
<td>self illum blend to full</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="remap-scalar-to-vector">Remap scalar to vector</h3>

<table>
<thead>
<tr>
<th>Remap scalar to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RemapScalarToVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>193</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Upon particle initialization, remap any starting scalar (alpha, radius, etc.) to any starting vector (position, color, etc.)</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>output min</td>
<td>vector</td>
</tr>
<tr>
<td>output max</td>
<td>vector</td>
</tr>
<tr>
<td>field input</td>
<td>integer</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>scale initial range</td>
<td>boolean</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>local coords</td>
<td>boolean</td>
</tr>
<tr>
<td>input min</td>
<td>float</td>
</tr>
<tr>
<td>start time</td>
<td>float</td>
</tr>
<tr>
<td>end time</td>
<td>float</td>
</tr>
<tr>
<td>set method</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="vector-random">Vector random</h3>

<table>
<thead>
<tr>
<th>Vector random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RandomVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>183</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>max</td>
<td>vector</td>
</tr>
<tr>
<td>min</td>
<td>vector</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="position-along-path-random">Position along path random</h3>

<table>
<thead>
<tr>
<th>Position along path random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_CreateAlongPath</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>168</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Initializes particle positions randomly along a line between two control points.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>path params</td>
<td>path params (special)</td>
</tr>
<tr>
<td>max distance</td>
<td>float</td>
</tr>
<tr>
<td>use random C ps</td>
<td>boolean</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="position-along-path-sequential-1">Position along path sequential</h3>

<table>
<thead>
<tr>
<th>Position along path sequential</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_CreateSequentialPathV2</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>163</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Initializes particle positions sequentially along a line between two or more control points.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>num to assign</td>
<td>float</td>
</tr>
<tr>
<td>loop</td>
<td>boolean</td>
</tr>
<tr>
<td>save offset</td>
<td>boolean</td>
</tr>
<tr>
<td>CP pairs</td>
<td>boolean</td>
</tr>
<tr>
<td>path params</td>
<td>path params (special)</td>
</tr>
<tr>
<td>max distance</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="position-on-spiral-sphere">Position on spiral sphere</h3>

<table>
<thead>
<tr>
<th>Position on spiral sphere</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_CreateSpiralSphere</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>101</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>density</td>
<td>integer</td>
</tr>
<tr>
<td>initial radius</td>
<td>float</td>
</tr>
<tr>
<td>initial speed max</td>
<td>float</td>
</tr>
<tr>
<td>initial speed min</td>
<td>float</td>
</tr>
<tr>
<td>use particle count</td>
<td>boolean</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>override CP</td>
<td>integer</td>
</tr>
<tr>
<td>run for parent apply kill list</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="remap-qangie-in-cp-to-rotations">Remap QAngIe in CP to rotations</h3>

<table>
<thead>
<tr>
<th>Remap QAngIe in CP to rotations</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RemapQAnglesToRotation</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>91</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="radius-from-cp-object">Radius from CP object</h3>

<table>
<thead>
<tr>
<th>Radius from CP object</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RadiusFromCPObject</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>69</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>control point</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="globally-scale-initial-attributes">Globally Scale Initial Attributes</h3>

<table>
<thead>
<tr>
<th>Globally Scale Initial Attributes</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_GlobalScale</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>60</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>scale position</td>
<td>boolean</td>
</tr>
<tr>
<td>scale control point number</td>
<td>integer</td>
</tr>
<tr>
<td>scale</td>
<td>float</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>scale velocity</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="set-hitbox-to-closest-hitbox">Set hitbox to closest hitbox</h3>

<table>
<thead>
<tr>
<th>Set hitbox to closest hitbox</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_SetHitboxToClosest</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>48</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>hit box scale</td>
<td>float</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>hitbox set name</td>
<td>string</td>
</tr>
</tbody>
</table><h3 id="sequence-from-control-point">Sequence from control point</h3>

<table>
<thead>
<tr>
<th>Sequence from control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_SequenceFromCP</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>45</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>radius scale</td>
<td>boolean</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="position-from-parent-cache">Position from parent cache</h3>

<table>
<thead>
<tr>
<th>Position from parent cache</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_CreateFromPlaneCache</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>45</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>use normal</td>
<td>boolean</td>
</tr>
<tr>
<td>offset max</td>
<td>vector</td>
</tr>
<tr>
<td>offset min</td>
<td>vector</td>
</tr>
</tbody>
</table><h3 id="cull-relative-to-ray-trace-environment">Cull relative to ray trace environment</h3>

<table>
<thead>
<tr>
<th>Cull relative to ray trace environment</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RtEnvCull</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>44</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>cull on miss</td>
<td>boolean</td>
</tr>
<tr>
<td>use velocity</td>
<td>boolean</td>
</tr>
<tr>
<td>life adjust</td>
<td>boolean</td>
</tr>
<tr>
<td>test normal</td>
<td>vector</td>
</tr>
<tr>
<td>rt env name</td>
<td>string</td>
</tr>
</tbody>
</table><h3 id="position-from-control-points">Position from control points</h3>

<table>
<thead>
<tr>
<th>Position from control points</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_CreateFromCPs</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>38</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>min CP</td>
<td>integer</td>
</tr>
<tr>
<td>max CP</td>
<td>integer</td>
</tr>
<tr>
<td>dynamic CP count</td>
<td>float (special)</td>
</tr>
<tr>
<td>increment</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="init-cp-orientation-to-rotations">Init CP orientation to rotations</h3>

<table>
<thead>
<tr>
<th>Init CP orientation to rotations</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RemapCPOrientationToRotations</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>35</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation</td>
<td>vector</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="init-vec">Init Vec</h3>

<table>
<thead>
<tr>
<th>Init Vec</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_InitVec</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>29</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>input value</td>
<td>vector (special)</td>
</tr>
<tr>
<td>output field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="add-vector-to-vector">Add vector to vector</h3>

<table>
<thead>
<tr>
<th>Add vector to vector</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_AddVectorToVector</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>24</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>field input</td>
<td>integer</td>
</tr>
<tr>
<td>offset min</td>
<td>vector</td>
</tr>
<tr>
<td>offset max</td>
<td>vector</td>
</tr>
<tr>
<td>scale</td>
<td>vector</td>
</tr>
</tbody>
</table><h3 id="velocity-radial-random">Velocity radial random</h3>

<table>
<thead>
<tr>
<th>Velocity radial random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_VelocityRadialRandom</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>23</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>local coordinate system speed scale</td>
<td>vector</td>
</tr>
<tr>
<td>speed min</td>
<td>float</td>
</tr>
<tr>
<td>speed max</td>
<td>float</td>
</tr>
<tr>
<td>ignore delta</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="remap-speed-to-scalar-1">Remap speed to scalar</h3>

<table>
<thead>
<tr>
<th>Remap speed to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RemapSpeedToScalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>23</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Remaps either a control point’s speed (effect-level) or each particle’s speed (particle-level) to a scalar value.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>per particle</td>
<td>boolean</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>scale initial range</td>
<td>boolean</td>
</tr>
<tr>
<td>input min</td>
<td>float</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="lifetime-from-time-to-impact">Lifetime from time to impact</h3>

<table>
<thead>
<tr>
<th>Lifetime from time to impact</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_LifespanFromVelocity</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>22</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>trace tolerance</td>
<td>float</td>
</tr>
<tr>
<td>collision group name</td>
<td>string</td>
</tr>
<tr>
<td>max trace length</td>
<td>float</td>
</tr>
<tr>
<td>max planes</td>
<td>integer</td>
</tr>
<tr>
<td>component scale</td>
<td>vector</td>
</tr>
</tbody>
</table><h3 id="velocity-repulse-from-world">Velocity repulse from world</h3>

<table>
<thead>
<tr>
<th>Velocity repulse from world</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_InitialRepulsionVelocity</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>21</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>output max</td>
<td>vector</td>
</tr>
<tr>
<td>inherit</td>
<td>boolean</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>collision group name</td>
<td>string</td>
</tr>
<tr>
<td>trace length</td>
<td>float</td>
</tr>
<tr>
<td>child CP</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="alpha-window-threshold-random">Alpha window threshold random</h3>

<table>
<thead>
<tr>
<th>Alpha window threshold random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RandomAlphaWindowThreshold</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>18</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>max</td>
<td>float</td>
</tr>
<tr>
<td>min</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="position-with-phyllotaxis-distribution">Position with phyllotaxis distribution</h3>

<table>
<thead>
<tr>
<th>Position with phyllotaxis distribution</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_CreatePhyllotaxis</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>18</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>scale CP</td>
<td>integer</td>
</tr>
<tr>
<td>overall</td>
<td>float</td>
</tr>
<tr>
<td>rad per point to</td>
<td>float</td>
</tr>
<tr>
<td>min rad</td>
<td>float</td>
</tr>
<tr>
<td>dist bias</td>
<td>float</td>
</tr>
<tr>
<td>use local coords</td>
<td>boolean</td>
</tr>
<tr>
<td>rad cent core</td>
<td>float</td>
</tr>
<tr>
<td>angle</td>
<td>string</td>
</tr>
<tr>
<td>rad bias</td>
<td>float</td>
</tr>
<tr>
<td>rad per point</td>
<td>float</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="velocity-away-from-hitbox-random">Velocity away from hitbox random</h3>

<table>
<thead>
<tr>
<th>Velocity away from hitbox random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_InitialVelocityFromHitbox</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>11</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>velocity min</td>
<td>float</td>
</tr>
<tr>
<td>velocity max</td>
<td>float</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>hitbox set name</td>
<td>string</td>
</tr>
<tr>
<td>use bones</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="position-modify-offset-relative-to-control-point">Position modify offset relative to control point</h3>

<table>
<thead>
<tr>
<th>Position modify offset relative to control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_init_positionoffsettocp</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>8</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>
<h3 id="velocity-from-normal-random">Velocity from normal random</h3>

<table>
<thead>
<tr>
<th>Velocity from normal random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_VelocityFromNormal</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>6</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>speed min</td>
<td>float</td>
</tr>
<tr>
<td>speed max</td>
<td>float</td>
</tr>
<tr>
<td>ignore dt</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="remap-initial-game-visibility-to-scalar">Remap initial game visibility to scalar</h3>

<table>
<thead>
<tr>
<th>Remap initial game visibility to scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_RemapInitialVisibilityScalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>6</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>rotation field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="color-lit-per-particle">Color lit per particle</h3>

<table>
<thead>
<tr>
<th>Color lit per particle</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_ColorLitPerParticle</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>5</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>color min</td>
<td>vector</td>
</tr>
<tr>
<td>color max</td>
<td>vector</td>
</tr>
</tbody>
</table><h3 id="init-vector-attribute-from-a-list-of-values">Init vector attribute from a list of values</h3>

<table>
<thead>
<tr>
<th>Init vector attribute from a list of values</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_PointList</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>3</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>list</td>
<td>list (control point)</td>
</tr>
</tbody>
</table><h3 id="move-particles-between-2-control-points">Move particles between 2 control points</h3>

<table>
<thead>
<tr>
<th>Move particles between 2 control points</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_MoveBetweenPoints</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>3</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Moves the particles between 2 control points at a value between the minimum and maximum speed. Can be extremely useful for particle tracers, laser sights/beams, and Halo-esque sniper-rifle trails.</p><p><i>Note:</i> Normally, this initializer moves particles to the end control point and leaves them there (i.e., if new particles are created, they will spawn at the end control point and immediately vanish). To get around this, add a “Position Along Path Sequential” initializer with start and end control points of 0 ABOVE the “Move Particles Between 2 Control Points” entry.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>speed min</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>speed max</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>end control point number</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>end spread</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>trail bias</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>start offset</td>
<td>float</td>
<td>Offset of where the particles start relative to the starting control point and direction of movement.</td>
</tr>
</tbody>
</table><h3 id="position-modify-warp-from-scalar">Position modify warp from scalar</h3>

<table>
<thead>
<tr>
<th>Position modify warp from scalar</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_INIT_PositionWarpScalar</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>warp min</td>
<td>vector</td>
</tr>
<tr>
<td>warp max</td>
<td>vector</td>
</tr>
<tr>
<td>input value</td>
<td>float (special)</td>
</tr>
</tbody>
</table><h2 id="renderer">Renderer</h2>
<h3 id="render-sprites">Render sprites</h3>

<table>
<thead>
<tr>
<th>Render sprites</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RenderSprites</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>26773</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Renders single- and multiple-frame sprites.</p><p>Multi-frame sequences can be animated or used to provide visual variation.</p><p>render_sprites is the workhorse renderer, and the one you’re likely to be using most of the time.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>texture</td>
<td>resource</td>
<td><p>The source texture to be applied to each particle. Eligible files use the extension *.vtex.</p></td>
</tr>
<tr>
<td>self-illumination amount</td>
<td>float</td>
<td><p>The degree to which the <i>unlit</i> texture color adds to the lighting calculation.</p><p>The easiest way to think of it is as an ambient lighting value for the particle system. So 0.0 will result in a diffuse lit particle. 0.5 will result in a diffuse lit particle but with an added ambient lighting value of 0.5.</p></td>
</tr>
<tr>
<td>fit cycle to lifetime</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>animation rate</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>color scale</td>
<td>vector</td>
<td></td>
</tr>
<tr>
<td>sequence combine mode</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>zoom amount 1</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>start fade size</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>end fade size</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>animation rate 2</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>max visual size</td>
<td>float</td>
<td>Individual particles will never render larger than this number as a fraction of screen size. (0.5 is 50% of the screen)</td>
</tr>
<tr>
<td>overbright factor</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>add self amount</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>blend frames seq 0</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>saturate color pre alpha blend</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>use additive blending</td>
<td>boolean</td>
<td><p>Toggles whether particles will <a href="https://en.wikipedia.org/wiki/Additive_color">blend additively</a>.</p></td>
</tr>
<tr>
<td>orientation type</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>animate in FPS</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>depth bias</td>
<td>float</td>
<td>Offsets particle depth via the shader. This is more expensive than per particle offsets which can be achieved by using “visibility camera depth bias”</td>
</tr>
<tr>
<td>disable Z buffering</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>visibility inputs</td>
<td>visibility inputs (special)</td>
<td></td>
</tr>
<tr>
<td>radius scale</td>
<td>float (special)</td>
<td></td>
</tr>
<tr>
<td>mod 2X</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>min visual size</td>
<td>float</td>
<td>Individual particles will never render smaller than this number as a fraction of screen size. (0.5 is 50% of the screen)</td>
</tr>
<tr>
<td>source alpha value to map to zero</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>particle feathering</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>feathering max dist</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>feathering mode</td>
<td>integer</td>
<td>Activates Depth Feathering. On (If Possible) will always draw the system even if feathering isn’t available. On (Required) will suppress the system rendering if feathering isn’t available.</td>
</tr>
<tr>
<td>fog particles</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>refract</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>refract amount</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>refract blur type</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>gamma correct vertex colors</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>alpha scale</td>
<td>float (special)</td>
<td></td>
</tr>
<tr>
<td>refract blur radius</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>orientation control point</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>center X offset</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>tint by FOW</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>tint by global light</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>per vertex lighting</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>cannot be refracted</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>HSV shift control point</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>feathering min dist</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>source alpha value to map to one</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>additive alpha</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>color scale</td>
<td>vector (special)</td>
<td></td>
</tr>
<tr>
<td>outline color</td>
<td>vector</td>
<td></td>
</tr>
<tr>
<td>animation type</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>diffuse lighting amount</td>
<td>float</td>
<td><p>Degree to which particles will receive scene lighting, with 0 being completely unlit (dark).</p></td>
</tr>
<tr>
<td>lighten mode</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>distance alpha</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>edge softness start</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>edge softness end</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>outline alpha</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>normal texture</td>
<td>resource</td>
<td></td>
</tr>
<tr>
<td>color blend type</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>final texture scale U</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>final texture offset U</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>center Y offset</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>final texture offset V</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>final texture scale V</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>use yaw with normal aligned</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>normal map</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>sequence 0 alpha weight</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>reverse Z buffering</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>outline end 0</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>first sequence offset for right eye</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>sequence override</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>outline</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>sequence 0RGB weight</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>sequence 1RGB weight</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>sequence 1 alpha weight</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>outline start 0</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>outline end 1</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>soft edges</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>outline start 1</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>bump strength</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>notes</td>
<td>string</td>
<td>If you have comments for the specific usage of this operator in this system, add them here and they’ll be saved with the system.</td>
</tr>
<tr>
<td>sort method</td>
<td>integer</td>
<td></td>
</tr>
</tbody>
</table><h3 id="render-rope">Render rope</h3>

<table>
<thead>
<tr>
<th>Render rope</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RenderRopes</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>6160</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Ropes (which were named in a simpler time) are sequences of sprites streched across a set of points. Textures intended for use on rope particles are often tiled along one axis so they can be used to create long, thin, curved forms in 3D space.</p><p>Ropes can be difficult to work with, but are surprisingly powerful and versatile.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>overbright factor</td>
<td>float</td>
</tr>
<tr>
<td>add self amount</td>
<td>float</td>
</tr>
<tr>
<td>saturate color pre alpha blend</td>
<td>boolean</td>
</tr>
<tr>
<td>texture</td>
<td>resource</td>
</tr>
<tr>
<td>radius scale</td>
<td>float</td>
</tr>
<tr>
<td>final texture offset U</td>
<td>float</td>
</tr>
<tr>
<td>texture V world size</td>
<td>float</td>
</tr>
<tr>
<td>texture V offset</td>
<td>float</td>
</tr>
<tr>
<td>max tesselation</td>
<td>integer</td>
</tr>
<tr>
<td>min tesselation</td>
<td>integer</td>
</tr>
<tr>
<td>color scale</td>
<td>vector</td>
</tr>
<tr>
<td>sequence combine mode</td>
<td>integer</td>
</tr>
<tr>
<td>use additive blending</td>
<td>boolean</td>
</tr>
<tr>
<td>texture V scroll rate</td>
<td>float</td>
</tr>
<tr>
<td>visibility inputs</td>
<td>visibility inputs (special)</td>
</tr>
<tr>
<td>orientation type</td>
<td>integer</td>
</tr>
<tr>
<td>depth bias</td>
<td>float</td>
</tr>
<tr>
<td>scale CP2</td>
<td>integer</td>
</tr>
<tr>
<td>scale CP1</td>
<td>integer</td>
</tr>
<tr>
<td>disable Z buffering</td>
<td>boolean</td>
</tr>
<tr>
<td>refract</td>
<td>boolean</td>
</tr>
<tr>
<td>refract amount</td>
<td>float</td>
</tr>
<tr>
<td>refract blur radius</td>
<td>integer</td>
</tr>
<tr>
<td>refract blur type</td>
<td>integer</td>
</tr>
<tr>
<td>gamma correct vertex colors</td>
<td>boolean</td>
</tr>
<tr>
<td>final texture scale V</td>
<td>float</td>
</tr>
<tr>
<td>mod 2X</td>
<td>boolean</td>
</tr>
<tr>
<td>cannot be refracted</td>
<td>boolean</td>
</tr>
<tr>
<td>tess scale</td>
<td>float</td>
</tr>
<tr>
<td>source alpha value to map to one</td>
<td>float</td>
</tr>
<tr>
<td>use scalar for texture coordinate</td>
<td>boolean</td>
</tr>
<tr>
<td>scalar field for texture coordinate</td>
<td>integer</td>
</tr>
<tr>
<td>closed loop</td>
<td>boolean</td>
</tr>
<tr>
<td>HSV shift control point</td>
<td>integer</td>
</tr>
<tr>
<td>clamp V</td>
<td>boolean</td>
</tr>
<tr>
<td>color scale</td>
<td>vector (special)</td>
</tr>
<tr>
<td>alpha scale</td>
<td>float (special)</td>
</tr>
<tr>
<td>feathering mode</td>
<td>integer</td>
</tr>
<tr>
<td>tint by global light</td>
<td>boolean</td>
</tr>
<tr>
<td>self-illumination amount</td>
<td>float</td>
</tr>
<tr>
<td>animation rate</td>
<td>float</td>
</tr>
<tr>
<td>lighten mode</td>
<td>boolean</td>
</tr>
<tr>
<td>tint by FOW</td>
<td>boolean</td>
</tr>
<tr>
<td>fog particles</td>
<td>boolean</td>
</tr>
<tr>
<td>feathering min dist</td>
<td>float</td>
</tr>
<tr>
<td>final texture scale U</td>
<td>float</td>
</tr>
<tr>
<td>scale V size by control point distance</td>
<td>float</td>
</tr>
<tr>
<td>color blend type</td>
<td>integer</td>
</tr>
<tr>
<td>diffuse lighting amount</td>
<td>float</td>
</tr>
<tr>
<td>enable fading and clamping</td>
<td>boolean</td>
</tr>
<tr>
<td>blend frames seq 0</td>
<td>boolean</td>
</tr>
<tr>
<td>scalar attribute texture coord scale</td>
<td>float</td>
</tr>
<tr>
<td>generate normals</td>
<td>boolean</td>
</tr>
<tr>
<td>particle feathering</td>
<td>boolean</td>
</tr>
<tr>
<td>feathering max dist</td>
<td>float</td>
</tr>
<tr>
<td>radius taper</td>
<td>float</td>
</tr>
<tr>
<td>final texture offset V</td>
<td>float</td>
</tr>
<tr>
<td>scale V offset by control point distance</td>
<td>float</td>
</tr>
<tr>
<td>scale V scroll by control point distance</td>
<td>float</td>
</tr>
<tr>
<td>additive alpha</td>
<td>boolean</td>
</tr>
<tr>
<td>reverse Z buffering</td>
<td>boolean</td>
</tr>
<tr>
<td>texture V params CP</td>
<td>integer</td>
</tr>
<tr>
<td>write stencil on depth pass</td>
<td>boolean</td>
</tr>
<tr>
<td>source alpha value to map to zero</td>
<td>float</td>
</tr>
<tr>
<td>draw as opaque</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="render-sprite-trail">Render sprite trail</h3>

<table>
<thead>
<tr>
<th>Render sprite trail</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RenderTrails</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>3477</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Trails are sprites with additional built-in behavior that stretches them based on their speed over time.</p><p>Traditional use cases for trails include bullet tracers and sparks. Advanced users may also find them useful when particles need to be oriented in 3D space (a case that regular sprites handle poorly.)</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>overbright factor</td>
<td>float</td>
</tr>
<tr>
<td>texture</td>
<td>resource</td>
</tr>
<tr>
<td>length fade in time</td>
<td>float</td>
</tr>
<tr>
<td>ignore DT</td>
<td>boolean</td>
</tr>
<tr>
<td>vert crop field</td>
<td>integer</td>
</tr>
<tr>
<td>final texture offset V</td>
<td>float</td>
</tr>
<tr>
<td>use additive blending</td>
<td>boolean</td>
</tr>
<tr>
<td>source alpha value to map to one</td>
<td>float</td>
</tr>
<tr>
<td>min length</td>
<td>float</td>
</tr>
<tr>
<td>animation rate</td>
<td>float</td>
</tr>
<tr>
<td>max length</td>
<td>float</td>
</tr>
<tr>
<td>sequence combine mode</td>
<td>integer</td>
</tr>
<tr>
<td>add self amount</td>
<td>float</td>
</tr>
<tr>
<td>saturate color pre alpha blend</td>
<td>boolean</td>
</tr>
<tr>
<td>radius scale</td>
<td>float</td>
</tr>
<tr>
<td>end trail tint factor</td>
<td>vector</td>
</tr>
<tr>
<td>visibility inputs</td>
<td>visibility inputs (special)</td>
</tr>
<tr>
<td>start fade size</td>
<td>float</td>
</tr>
<tr>
<td>end fade size</td>
<td>float</td>
</tr>
<tr>
<td>max visual size</td>
<td>float</td>
</tr>
<tr>
<td>blend frames seq 0</td>
<td>boolean</td>
</tr>
<tr>
<td>feathering mode</td>
<td>integer</td>
</tr>
<tr>
<td>mod 2X</td>
<td>boolean</td>
</tr>
<tr>
<td>radius taper</td>
<td>float</td>
</tr>
<tr>
<td>final texture scale V</td>
<td>float</td>
</tr>
<tr>
<td>particle feathering</td>
<td>boolean</td>
</tr>
<tr>
<td>disable Z buffering</td>
<td>boolean</td>
</tr>
<tr>
<td>length scale</td>
<td>float</td>
</tr>
<tr>
<td>constrain radius to length ratio</td>
<td>float</td>
</tr>
<tr>
<td>source alpha value to map to zero</td>
<td>float</td>
</tr>
<tr>
<td>depth bias</td>
<td>float</td>
</tr>
<tr>
<td>tail color scale</td>
<td>vector (special)</td>
</tr>
<tr>
<td>tail alpha scale</td>
<td>float (special)</td>
</tr>
<tr>
<td>HSV shift control point</td>
<td>integer</td>
</tr>
<tr>
<td>feathering max dist</td>
<td>float</td>
</tr>
<tr>
<td>horiz crop field</td>
<td>integer</td>
</tr>
<tr>
<td>orientation type</td>
<td>integer</td>
</tr>
<tr>
<td>final texture offset U</td>
<td>float</td>
</tr>
<tr>
<td>flip UV based on pitch yaw</td>
<td>boolean</td>
</tr>
<tr>
<td>feathering min dist</td>
<td>float</td>
</tr>
<tr>
<td>alpha scale</td>
<td>float (special)</td>
</tr>
<tr>
<td>color scale</td>
<td>vector</td>
</tr>
<tr>
<td>self-illumination amount</td>
<td>float</td>
</tr>
<tr>
<td>use topology</td>
<td>boolean</td>
</tr>
<tr>
<td>enable fading and clamping</td>
<td>boolean</td>
</tr>
<tr>
<td>min visual size</td>
<td>float</td>
</tr>
<tr>
<td>orientation control point</td>
<td>integer</td>
</tr>
<tr>
<td>forward shift</td>
<td>float</td>
</tr>
<tr>
<td>diffuse lighting amount</td>
<td>float</td>
</tr>
<tr>
<td>gamma correct vertex colors</td>
<td>boolean</td>
</tr>
<tr>
<td>additive alpha</td>
<td>boolean</td>
</tr>
<tr>
<td>prev pnt source</td>
<td>integer</td>
</tr>
<tr>
<td>lighten mode</td>
<td>boolean</td>
</tr>
<tr>
<td>fit cycle to lifetime</td>
<td>boolean</td>
</tr>
<tr>
<td>animate in FPS</td>
<td>boolean</td>
</tr>
<tr>
<td>tint by FOW</td>
<td>boolean</td>
</tr>
<tr>
<td>animation type</td>
<td>integer</td>
</tr>
<tr>
<td>refract</td>
<td>boolean</td>
</tr>
<tr>
<td>refract amount</td>
<td>float</td>
</tr>
<tr>
<td>refract blur radius</td>
<td>integer</td>
</tr>
<tr>
<td>refract blur type</td>
<td>integer</td>
</tr>
<tr>
<td>radius head taper</td>
<td>float (special)</td>
</tr>
<tr>
<td>head alpha scale</td>
<td>float (special)</td>
</tr>
<tr>
<td>color scale</td>
<td>vector (special)</td>
</tr>
<tr>
<td>head color scale</td>
<td>vector (special)</td>
</tr>
<tr>
<td>cannot be refracted</td>
<td>boolean</td>
</tr>
<tr>
<td>final texture scale U</td>
<td>float</td>
</tr>
<tr>
<td>clamp V</td>
<td>boolean</td>
</tr>
<tr>
<td>tint by global light</td>
<td>boolean</td>
</tr>
<tr>
<td>fog particles</td>
<td>boolean</td>
</tr>
<tr>
<td>per vertex lighting</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="render-deferred-light">Render deferred light</h3>

<table>
<thead>
<tr>
<th>Render deferred light</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RenderDeferredLight</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1943</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Renders one or more real-time (but not shadow-casting) light sources based on particle positions.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>color scale</td>
<td>vector</td>
</tr>
<tr>
<td>use texture</td>
<td>boolean</td>
</tr>
<tr>
<td>alpha scale</td>
<td>float</td>
</tr>
<tr>
<td>start falloff</td>
<td>float</td>
</tr>
<tr>
<td>texture</td>
<td>resource</td>
</tr>
<tr>
<td>radius scale</td>
<td>float</td>
</tr>
<tr>
<td>spot fo V</td>
<td>float</td>
</tr>
<tr>
<td>distance falloff</td>
<td>float</td>
</tr>
<tr>
<td>light distance</td>
<td>float</td>
</tr>
<tr>
<td>color scale</td>
<td>vector (special)</td>
</tr>
<tr>
<td>use alpha test window</td>
<td>boolean</td>
</tr>
<tr>
<td>alpha test sharpness field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="render-projected">Render projected</h3>

<table>
<thead>
<tr>
<th>Render projected</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RenderProjected</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>591</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Renders projected textures, which are capable of certain behaviors that are otherwise difficult to achieve.</p><p>Take, for example, a large scorch-mark on the ground. If you used a flat sprite (even one oriented to the ground polygon on which it sat), it still wouldn’t look right if it crossed polygon boundaries that changed angles or elevation. A projected texture, however, will conform to the surfaces upon which it’s projected.</p><p><i>Note that unlike many other effect renderers, this one takes a VMAT rather than a VTEX. VMATs are authored in the Material Editor, and should be shader type “Projected Dota”.</i></p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>projected material</td>
<td>resource</td>
</tr>
<tr>
<td>flip horizontal</td>
<td>boolean</td>
</tr>
<tr>
<td>project water</td>
<td>boolean</td>
</tr>
<tr>
<td>enable projected depth controls</td>
<td>boolean</td>
</tr>
<tr>
<td>max projection depth</td>
<td>float</td>
</tr>
<tr>
<td>min projection depth</td>
<td>float</td>
</tr>
<tr>
<td>project character</td>
<td>boolean</td>
</tr>
<tr>
<td>HSV shift control point</td>
<td>integer</td>
</tr>
<tr>
<td>cannot be refracted</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="render-status-effect">Render Status Effect</h3>

<table>
<thead>
<tr>
<th>Render Status Effect</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RenderStatusEffect</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>199</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>texture color warp</td>
<td>texture</td>
</tr>
<tr>
<td>texture detail 2</td>
<td>texture</td>
</tr>
<tr>
<td>texture diffuse warp</td>
<td>texture</td>
</tr>
<tr>
<td>texture fresnel color warp</td>
<td>texture</td>
</tr>
<tr>
<td>texture fresnel warp</td>
<td>texture</td>
</tr>
<tr>
<td>texture specular warp</td>
<td>texture</td>
</tr>
<tr>
<td>texture env map</td>
<td>texture</td>
</tr>
</tbody>
</table><h3 id="render-screen-shake">Render screen shake</h3>

<table>
<thead>
<tr>
<th>Render screen shake</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RenderScreenShake</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>132</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>amplitude scale</td>
<td>float</td>
</tr>
<tr>
<td>frequency scale</td>
<td>float</td>
</tr>
<tr>
<td>radius scale</td>
<td>float</td>
</tr>
<tr>
<td>duration scale</td>
<td>float</td>
</tr>
<tr>
<td>amplitude field</td>
<td>integer</td>
</tr>
<tr>
<td>filter CP</td>
<td>integer</td>
</tr>
<tr>
<td>frequency field</td>
<td>integer</td>
</tr>
<tr>
<td>radius field</td>
<td>integer</td>
</tr>
<tr>
<td>duration field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="render-blobs">Render blobs</h3>

<table>
<thead>
<tr>
<th>Render blobs</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RenderBlobs</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>55</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>width</td>
<td>float</td>
</tr>
<tr>
<td>radius</td>
<td>float</td>
</tr>
<tr>
<td>radius</td>
<td>float</td>
</tr>
<tr>
<td>material</td>
<td>resource</td>
</tr>
<tr>
<td>scale CP</td>
<td>integer</td>
</tr>
<tr>
<td>cannot be refracted</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="render-sound">Render sound</h3>

<table>
<thead>
<tr>
<th>Render sound</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RenderSound</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>13</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>sound name</td>
<td>sound name</td>
</tr>
<tr>
<td>snd lvl scale</td>
<td>float</td>
</tr>
<tr>
<td>volume field</td>
<td>integer</td>
</tr>
<tr>
<td>pitch field</td>
<td>integer</td>
</tr>
<tr>
<td>duration field</td>
<td>integer</td>
</tr>
<tr>
<td>volume scale</td>
<td>float</td>
</tr>
<tr>
<td>pitch scale</td>
<td>float</td>
</tr>
<tr>
<td>duration scale</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="render-tree-shake">Render Tree Shake</h3>

<table>
<thead>
<tr>
<th>Render Tree Shake</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RenderTreeShake</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>peak strength</td>
<td>float</td>
</tr>
<tr>
<td>radius</td>
<td>float</td>
</tr>
<tr>
<td>transition time</td>
<td>float</td>
</tr>
<tr>
<td>shake duration</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="render-text">Render Text</h3>

<table>
<thead>
<tr>
<th>Render Text</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RenderText</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>outline color</td>
<td>vector</td>
</tr>
</tbody>
</table><h2 id="emitter">Emitter</h2>
<h3 id="emit-continuously">Emit continuously</h3>

<table>
<thead>
<tr>
<th>Emit continuously</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_ContinuousEmitter</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>20922</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Emits particles at the specified rate over time. By default, this emitter will continue to emit forever.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>emit rate</td>
<td>float</td>
<td>Number of particles to spawn (per second).</td>
</tr>
<tr>
<td>emission duration</td>
<td>float</td>
<td>Length of time to continue emitting particles (seconds).</td>
</tr>
<tr>
<td>start time</td>
<td>float (special)</td>
<td>Time at which to begin emitting particles (seconds).</td>
</tr>
<tr>
<td>init from killed parent particles</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>scale per parent particle</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>scale control point</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>scale control point field</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>scale per particle</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>emission scale</td>
<td>float</td>
<td></td>
</tr>
</tbody>
</table><h3 id="emit-instantaniously">Emit instantaniously</h3>

<table>
<thead>
<tr>
<th>Emit instantaniously</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_InstantaneousEmitter</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>18907</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Emits the specified number of particles all at once and never repeats.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>particles to emit</td>
<td>integer</td>
<td>Number of particles to emit in a burst.</td>
</tr>
<tr>
<td>start time</td>
<td>float</td>
<td>Time at which to begin emitting particles (seconds).</td>
</tr>
<tr>
<td>snapshot control point</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>max emitted per frame</td>
<td>integer</td>
<td><p>The maximum number of particles to emit per frame.</p><p>For example, if the game is running at 30 frames per second and this value is set to 1, then 30 particles will be emitted in one second. Keep in mind that even though the particles are emitted at a different time, they will all die together at the same time. Therefore, if lifetime random is set to 2, then every particle regardless of when it was created will be removed after 2 seconds of the system’s lifetime.</p></td>
</tr>
<tr>
<td>scale control point field</td>
<td>integer</td>
<td></td>
</tr>
<tr>
<td>init from killed parent particles</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>min particles to emit</td>
<td>integer</td>
<td><p>The minimum number of particles to emit in a burst. Any value other than -1 will tell the system to randomly emit a number of particles between this value and the num_to_emit value.</p></td>
</tr>
<tr>
<td>start time max</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>scale control point</td>
<td>integer</td>
<td></td>
</tr>
</tbody>
</table><h3 id="emit-noise">Emit noise</h3>

<table>
<thead>
<tr>
<th>Emit noise</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_NoiseEmitter</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1385</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>noise scale</td>
<td>float</td>
</tr>
<tr>
<td>world time scale</td>
<td>float</td>
</tr>
<tr>
<td>emission duration</td>
<td>float</td>
</tr>
<tr>
<td>scale control point</td>
<td>integer</td>
</tr>
<tr>
<td>offset</td>
<td>float</td>
</tr>
<tr>
<td>start time</td>
<td>float</td>
</tr>
<tr>
<td>noise scale loc</td>
<td>float</td>
</tr>
<tr>
<td>offset loc</td>
<td>vector</td>
</tr>
<tr>
<td>abs val</td>
<td>boolean</td>
</tr>
<tr>
<td>world noise scale</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="emit-to-maintain-count">Emit to maintain count</h3>

<table>
<thead>
<tr>
<th>Emit to maintain count</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_MaintainEmitter</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>133</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Emits particles until it reaches the specified <b>count to maintain</b>, and then stops. Whenever particles are destroyed (by whatever means), the emitter will kick in again to bring the count back up to the max.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>particles to maintain</td>
<td>integer</td>
</tr>
<tr>
<td>start time</td>
<td>float</td>
</tr>
<tr>
<td>scale control point</td>
<td>integer</td>
</tr>
<tr>
<td>scale control point field</td>
<td>integer</td>
</tr>
</tbody>
</table><h2 id="force-gen">Force-Gen</h2>
<h3 id="pull-towards-control-point">Pull towards control point</h3>

<table>
<thead>
<tr>
<th>Pull towards control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_AttractToControlPoint</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>3868</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Pulls particles toward the specified control point.</p><p>Can also be used to repel particles - simply use negative values for <b>amount of force</b>.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>force amount</td>
<td>float</td>
</tr>
<tr>
<td>falloff power</td>
<td>float</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>force amount min</td>
<td>float</td>
</tr>
<tr>
<td>component scale</td>
<td>vector</td>
</tr>
<tr>
<td>apply min force</td>
<td>boolean</td>
</tr>
<tr>
<td>scale local</td>
<td>boolean</td>
</tr>
<tr>
<td>remap pull force to life</td>
<td>boolean</td>
</tr>
<tr>
<td>scale CP field</td>
<td>integer</td>
</tr>
<tr>
<td>scale CP</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="random-force">Random force</h3>

<table>
<thead>
<tr>
<th>Random force</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RandomForce</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1092</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Generates a random force within the specified range that’s applied uniformly to all particles within the effect.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>max force</td>
<td>vector</td>
</tr>
<tr>
<td>min force</td>
<td>vector</td>
</tr>
</tbody>
</table><h3 id="twist-around-axis">Twist around axis</h3>

<table>
<thead>
<tr>
<th>Twist around axis</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_TwistAroundAxis</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>860</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>force amount</td>
<td>float</td>
</tr>
<tr>
<td>use local space</td>
<td>boolean</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>twist axis</td>
<td>vector</td>
</tr>
</tbody>
</table><h3 id="curlnoise-force">CurlNoise force</h3>

<table>
<thead>
<tr>
<th>CurlNoise force</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_CurlNoiseForce</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>329</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>noise freq</td>
<td>vector</td>
<td></td>
</tr>
<tr>
<td>noise scale</td>
<td>vector</td>
<td>Amplitude of the noise</td>
</tr>
<tr>
<td>offset rate</td>
<td>vector</td>
<td>This will increment the noise offset each frame</td>
</tr>
<tr>
<td>curl</td>
<td>boolean</td>
<td>toggle between dnoise() and curlnoise()</td>
</tr>
</tbody>
</table><h3 id="turbulent-force">Turbulent force</h3>

<table>
<thead>
<tr>
<th>Turbulent force</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_TurbulenceForce</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>204</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>noise amount 3</td>
<td>vector</td>
</tr>
<tr>
<td>noise coord scale 3</td>
<td>float</td>
</tr>
<tr>
<td>noise amount 2</td>
<td>vector</td>
</tr>
<tr>
<td>noise coord scale 2</td>
<td>float</td>
</tr>
<tr>
<td>noise amount 1</td>
<td>vector</td>
</tr>
<tr>
<td>noise coord scale 1</td>
<td>float</td>
</tr>
<tr>
<td>noise amount 0</td>
<td>vector</td>
</tr>
<tr>
<td>noise coord scale 0</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="external-wind-force">External Wind force</h3>

<table>
<thead>
<tr>
<th>External Wind force</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_ExternalWindForce</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>135</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>scale</td>
<td>vector</td>
</tr>
</tbody>
</table><h3 id="local-acceleraton-force">Local acceleraton force</h3>

<table>
<thead>
<tr>
<th>Local acceleraton force</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_LocalAccelerationForce</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>105</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>accel</td>
<td>vector</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="time-varying-force">Time varying force</h3>

<table>
<thead>
<tr>
<th>Time varying force</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_TimeVaryingForce</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>55</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>end lerp time</td>
<td>float</td>
</tr>
<tr>
<td>ending force</td>
<td>vector</td>
</tr>
<tr>
<td>starting force</td>
<td>vector</td>
</tr>
<tr>
<td>start lerp time</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="force-based-on-distance-from-plane">Force based on distance from plane</h3>

<table>
<thead>
<tr>
<th>Force based on distance from plane</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_ForceBasedOnDistanceToPlane</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>19</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Applies a force to each particle based on its distance from a specified plane. (You can think of this as simply remapping a distance to a force range.)</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>force at min dist</td>
<td>vector</td>
</tr>
<tr>
<td>max dist</td>
<td>float</td>
</tr>
<tr>
<td>min dist</td>
<td>float</td>
</tr>
<tr>
<td>force at max dist</td>
<td>vector</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="create-vortices-from-parent-particles">Create vortices from parent particles</h3>

<table>
<thead>
<tr>
<th>Create vortices from parent particles</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_ParentVortices</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>16</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>force scale</td>
<td>float</td>
</tr>
<tr>
<td>flip based on yaw</td>
<td>boolean</td>
</tr>
</tbody>
</table><h2 id="pre">Pre</h2>
<h3 id="set-single-control-point-position">Set single control point position</h3>

<table>
<thead>
<tr>
<th>Set single control point position</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetSingleControlPointPosition</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2679</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Allows the manual positioning of a single control point.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>CP1 pos</td>
<td>vector</td>
</tr>
<tr>
<td>CP1</td>
<td>integer</td>
</tr>
<tr>
<td>head location</td>
<td>integer</td>
</tr>
<tr>
<td>set once</td>
<td>boolean</td>
</tr>
<tr>
<td>use world location</td>
<td>boolean</td>
</tr>
<tr>
<td>notes</td>
<td>string</td>
</tr>
</tbody>
</table><h3 id="set-control-point-orientaton">Set control point orientaton</h3>

<table>
<thead>
<tr>
<th>Set control point orientaton</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetControlPointOrientation</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1240</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rotation</td>
<td>vector</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>head location</td>
<td>integer</td>
</tr>
<tr>
<td>set once</td>
<td>boolean</td>
</tr>
<tr>
<td>rotation B</td>
<td>vector</td>
</tr>
<tr>
<td>use world location</td>
<td>boolean</td>
</tr>
<tr>
<td>randomize</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="set-control-point-positions">Set control point Positions</h3>

<table>
<thead>
<tr>
<th>Set control point Positions</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetControlPointPositions</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1039</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Allows the manual positioning of up to four control points.</p><p>If you’re only setting one CP, consider using “Set Single Control Point Position” instead.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>orient</td>
<td>boolean</td>
</tr>
<tr>
<td>CP1</td>
<td>integer</td>
</tr>
<tr>
<td>CP2</td>
<td>integer</td>
</tr>
<tr>
<td>CP3</td>
<td>integer</td>
</tr>
<tr>
<td>CP4</td>
<td>integer</td>
</tr>
<tr>
<td>CP1 pos</td>
<td>vector</td>
</tr>
<tr>
<td>CP2 pos</td>
<td>vector</td>
</tr>
<tr>
<td>CP3 pos</td>
<td>vector</td>
</tr>
<tr>
<td>CP4 pos</td>
<td>vector</td>
</tr>
<tr>
<td>head location</td>
<td>integer</td>
</tr>
<tr>
<td>CP1 parent</td>
<td>integer</td>
</tr>
<tr>
<td>CP2 parent</td>
<td>integer</td>
</tr>
<tr>
<td>CP3 parent</td>
<td>integer</td>
</tr>
<tr>
<td>CP4 parent</td>
<td>integer</td>
</tr>
<tr>
<td>use world location</td>
<td>boolean</td>
</tr>
<tr>
<td>set once</td>
<td>boolean</td>
</tr>
<tr>
<td>notes</td>
<td>string</td>
</tr>
</tbody>
</table><h3 id="set-per-child-control-point-from-parent-control-points">Set per child control point from parent control points</h3>

<table>
<thead>
<tr>
<th>Set per child control point from parent control points</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetParentControlPointsToChildCP</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>716</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>child control point</td>
<td>integer</td>
</tr>
<tr>
<td>num control points</td>
<td>integer</td>
</tr>
<tr>
<td>first source point</td>
<td>integer</td>
</tr>
<tr>
<td>set orientation</td>
<td>boolean</td>
</tr>
<tr>
<td>child group ID</td>
<td>integer</td>
</tr>
<tr>
<td>notes</td>
<td>string</td>
</tr>
</tbody>
</table><h3 id="remap-cp-speed-to-cp">Remap CP speed to CP</h3>

<table>
<thead>
<tr>
<th>Remap CP speed to CP</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapSpeedtoCP</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>656</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>out control point number</td>
<td>integer</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>input min</td>
<td>float</td>
</tr>
<tr>
<td>in control point number</td>
<td>integer</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="hsv-shift-to-control-point">HSV Shift to control point</h3>

<table>
<thead>
<tr>
<th>HSV Shift to control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_HSVShiftToCP</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>584</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>default HSV color</td>
<td>vector</td>
</tr>
<tr>
<td>notes</td>
<td>string</td>
</tr>
</tbody>
</table><h3 id="stop-effect-after-duraton">Stop effect after duraton</h3>

<table>
<thead>
<tr>
<th>Stop effect after duraton</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_StopAfterCPDuration</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>520</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>duration</td>
<td>float</td>
</tr>
<tr>
<td>destroy immediately</td>
<td>boolean</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>play end cap</td>
<td>boolean</td>
</tr>
<tr>
<td>CP field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="set-control-point-from-cp-object-scale">Set control point from CP object scale</h3>

<table>
<thead>
<tr>
<th>Set control point from CP object scale</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetControlPointFromObjectScale</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>462</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>CP output</td>
<td>integer</td>
</tr>
<tr>
<td>CP input</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="set-control-point-rotation">Set control point rotation</h3>

<table>
<thead>
<tr>
<th>Set control point rotation</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetControlPointRotation</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>300</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rot axis</td>
<td>vector</td>
</tr>
<tr>
<td>rot rate</td>
<td>float</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>local CP</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="set-control-point-to-random-position">Set control point to random Position</h3>

<table>
<thead>
<tr>
<th>Set control point to random Position</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetRandomControlPointPosition</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>131</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>CP1</td>
<td>integer</td>
</tr>
<tr>
<td>CP min pos</td>
<td>vector</td>
</tr>
<tr>
<td>CP max pos</td>
<td>vector</td>
</tr>
<tr>
<td>use world location</td>
<td>boolean</td>
</tr>
<tr>
<td>re random rate</td>
<td>float</td>
</tr>
<tr>
<td>head location</td>
<td>integer</td>
</tr>
<tr>
<td>orient</td>
<td>boolean</td>
</tr>
<tr>
<td>notes</td>
<td>string</td>
</tr>
</tbody>
</table><h3 id="set-cp-orientaton-to-point-at-second-cp">Set CP orientaton to point at second CP</h3>

<table>
<thead>
<tr>
<th>Set CP orientaton to point at second CP</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetCPOrientationToPointAtCP</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>69</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>output CP</td>
<td>integer</td>
</tr>
<tr>
<td>input CP</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="remap-average-scalar-value-to-cp">Remap average scalar value to CP</h3>

<table>
<thead>
<tr>
<th>Remap average scalar value to CP</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapAverageScalarValuetoCP</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>51</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>out control point number</td>
<td>integer</td>
</tr>
<tr>
<td>field</td>
<td>integer</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>out vector field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="remap-cp-component-to-cp-component">Remap CP component to CP component</h3>

<table>
<thead>
<tr>
<th>Remap CP component to CP component</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RemapCPtoCP</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>47</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>input control point</td>
<td>integer</td>
</tr>
<tr>
<td>output control point</td>
<td>integer</td>
</tr>
<tr>
<td>output min</td>
<td>float</td>
</tr>
<tr>
<td>output max</td>
<td>float</td>
</tr>
<tr>
<td>input max</td>
<td>float</td>
</tr>
<tr>
<td>input min</td>
<td>float</td>
</tr>
<tr>
<td>input field</td>
<td>integer</td>
</tr>
<tr>
<td>output field</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="set-control-point-to-impact-point">Set control point to impact point</h3>

<table>
<thead>
<tr>
<th>Set control point to impact point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetControlPointToImpactPoint</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>32</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>trace dir</td>
<td>vector</td>
</tr>
<tr>
<td>CP out</td>
<td>integer</td>
</tr>
<tr>
<td>CP in</td>
<td>integer</td>
</tr>
<tr>
<td>offset</td>
<td>float</td>
</tr>
<tr>
<td>collision group name</td>
<td>string</td>
</tr>
<tr>
<td>trace length</td>
<td>float</td>
</tr>
<tr>
<td>update rate</td>
<td>float</td>
</tr>
</tbody>
</table><h3 id="force-control-point-in-pet">Force Control Point In Pet</h3>

<table>
<thead>
<tr>
<th>Force Control Point In Pet</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_ForceControlPointStub</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>31</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>control point</td>
<td>string</td>
</tr>
</tbody>
</table><h3 id="enable-children-from-parent-particle-count">Enable children from parent particle count</h3>

<table>
<thead>
<tr>
<th>Enable children from parent particle count</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_EnableChildrenFromParentParticleCount</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>27</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>num children to enable</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="repeatedly-trigger-child-group">Repeatedly Trigger Child Group</h3>

<table>
<thead>
<tr>
<th>Repeatedly Trigger Child Group</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RepeatedTriggerChildGroup</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>9</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>child group ID</td>
<td>integer</td>
<td>Children with this Group ID specified will not fire when the system is created.Instead, they will fire based on the settings of this operator.  Group ID is available under the Base Properties as an Advanced Option of all particle systems.</td>
</tr>
<tr>
<td>cluster refire time</td>
<td>float (special)</td>
<td>Time/RandRange/Etc. for firing off children</td>
</tr>
<tr>
<td>cluster size</td>
<td>float (special)</td>
<td>Number of children to fire before entering cooldown</td>
</tr>
<tr>
<td>cluster cooldown</td>
<td>float (special)</td>
<td>Cooldown between clusters of firings</td>
</tr>
</tbody>
</table><h3 id="set-control-point-component-to-scalar-expression">Set control point component to scalar expression</h3>

<table>
<thead>
<tr>
<th>Set control point component to scalar expression</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetControlPointFieldToScalarExpression</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>5</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>input 1</td>
<td>float (special)</td>
</tr>
<tr>
<td>output CP</td>
<td>integer</td>
</tr>
<tr>
<td>expression</td>
<td>integer</td>
</tr>
<tr>
<td>input 2</td>
<td>float (special)</td>
</tr>
</tbody>
</table><h3 id="ramp-control-point-linear-random">Ramp control point linear random</h3>

<table>
<thead>
<tr>
<th>Ramp control point linear random</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RampCPLinearRandom</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>4</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>out control point number</td>
<td>integer</td>
</tr>
<tr>
<td>rate min</td>
<td>vector</td>
</tr>
<tr>
<td>rate max</td>
<td>vector</td>
</tr>
</tbody>
</table><h3 id="use-random-children-in-group">Use Random Children in Group</h3>

<table>
<thead>
<tr>
<th>Use Random Children in Group</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_ChooseRandomChildrenInGroup</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>4</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>child group ID</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="set-dest-cp-field-1-if-source-cp-is-in-water">Set dest CP field 1 if source CP is in water</h3>

<table>
<thead>
<tr>
<th>Set dest CP field 1 if source CP is in water</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_SetControlPointFieldToWater</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>dest CP</td>
<td>integer</td>
</tr>
</tbody>
</table><h2 id="constraint">Constraint</h2>
<h3 id="constrain-distance-to-control-point">Constrain distance to control point</h3>

<table>
<thead>
<tr>
<th>Constrain distance to control point</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_ConstrainDistance</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>446</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Locks particles’s positions to a specified radial range from a control point.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>max distance</td>
<td>float</td>
</tr>
<tr>
<td>min distance</td>
<td>float</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>center offset</td>
<td>vector</td>
</tr>
<tr>
<td>scale CP</td>
<td>integer</td>
</tr>
<tr>
<td>global center</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="collision-via-traces">Collision via traces</h3>

<table>
<thead>
<tr>
<th>Collision via traces</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_WorldTraceConstraint</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>318</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td><p>Allows particles to collide with scene geometry.</p><p><b>USE SPARINGLY!</b> Per-particle collision is one of the most expensive effects operations performance-wise. Also, make sure you always replace the <b>collision group</b> property “NONE” with “DEBRIS”.</p></td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>collision group name</td>
<td>string</td>
<td></td>
</tr>
<tr>
<td>bounce amount</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>slide amount</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>killon contact</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>collision mode</td>
<td>integer</td>
<td>Colission Modes :#define COLLISION_MODE_PER_PARTICLE_TRACE 0#define COLLISION_MODE_PER_FRAME_PLANESET 1#define COLLISION_MODE_INITIAL_TRACE_DOWN 2#define COLLISION_MODE_USE_NEAREST_TRACE 3</td>
</tr>
<tr>
<td>radius scale</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>set normal</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>brush only</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>cp offset</td>
<td>vector</td>
<td>-----</td>
</tr>
<tr>
<td>confirm collision</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>decay bounce</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>random dir scale</td>
<td>float (special)</td>
<td></td>
</tr>
<tr>
<td>stop speed</td>
<td>float (special)</td>
<td></td>
</tr>
<tr>
<td>trace tolerance</td>
<td>float</td>
<td></td>
</tr>
<tr>
<td>world only</td>
<td>boolean</td>
<td></td>
</tr>
<tr>
<td>cp movement tolerance</td>
<td>float</td>
<td></td>
</tr>
</tbody>
</table><h3 id="prevent-passing-through-a-plane">Prevent passing through a plane</h3>

<table>
<thead>
<tr>
<th>Prevent passing through a plane</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_PlanarConstraint</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>312</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>global normal</td>
<td>boolean</td>
</tr>
<tr>
<td>point on plane</td>
<td>vector</td>
</tr>
<tr>
<td>plane normal</td>
<td>vector</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>global origin</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="constrain-distance-to-path-between-two-control-points">Constrain distance to path between two control points</h3>

<table>
<thead>
<tr>
<th>Constrain distance to path between two control points</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_ConstrainDistanceToPath</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>306</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>travel time</td>
<td>float</td>
</tr>
<tr>
<td>max distance 0</td>
<td>float</td>
</tr>
<tr>
<td>path parameters</td>
<td>path params (special)</td>
</tr>
<tr>
<td>max distance mid</td>
<td>float</td>
</tr>
<tr>
<td>max distance 1</td>
<td>float</td>
</tr>
<tr>
<td>min distance</td>
<td>float</td>
</tr>
<tr>
<td>manual T field</td>
<td>integer</td>
</tr>
<tr>
<td>field scale</td>
<td>integer</td>
</tr>
</tbody>
</table><h3 id="constrain-particles-to-a-box">Constrain particles to a box</h3>

<table>
<thead>
<tr>
<th>Constrain particles to a box</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_BoxConstraint</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>23</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>min</td>
<td>vector</td>
</tr>
<tr>
<td>max</td>
<td>vector</td>
</tr>
<tr>
<td>control point number</td>
<td>integer</td>
</tr>
<tr>
<td>use local space</td>
<td>boolean</td>
</tr>
</tbody>
</table><h3 id="prevent-passing-through-static-part-of-world">Prevent passing through static part of world</h3>

<table>
<thead>
<tr>
<th>Prevent passing through static part of world</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>c_op_worldcollideconstraint</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>2</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>
<h3 id="rope-spring-constraint">Rope Spring constraint</h3>

<table>
<thead>
<tr>
<th>Rope Spring constraint</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td><code>C_OP_RopeSpringConstraint</code></td>
</tr>
<tr>
<td>Usage Count</td>
<td>1</td>
</tr>
<tr>
<td>Description (Valve)</td>
<td>------------------</td>
</tr>
<tr>
<td>Additional Notes</td>
<td>------------------</td>
</tr>
</tbody>
</table><hr>

<table>
<thead>
<tr>
<th>Fields</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>rest length</td>
<td>float (special)</td>
</tr>
<tr>
<td>max distance</td>
<td>float (special)</td>
</tr>
</tbody>
</table>
