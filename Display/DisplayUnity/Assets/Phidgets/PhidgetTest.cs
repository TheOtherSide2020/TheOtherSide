// Entertainment Technology Center, Carnegie Mellon University
// Building Virtual Worlds
// Caleb Biasco, 2018

// BVW2019 Update Log: 
//      - Updated part of the comments
//      - Updated the try-catch code
//      - Updated some new phidgets
//      - Made the code more readable
// By Xiangyu (Shawn) Sun

// To see this code in action for find more explanations of the Phidgets,
// go to https://wiki.etc.cmu.edu/index.php/Phidgets

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Phidget22;

// This Phidget test uses a VINT Hub with the following Phidgets attached to each of the 6 ports:
// (1) Slider 60mm
// (2) Dial Phidget
// (3) Thumbstick Phidget
// (4) Rotation Sensor 10 Turn
// (5) Touch Sensor
// (6) Magnetic Sensor
// Make sure to remove anything you are not using before using this as a test case!

public class PhidgetTest : MonoBehaviour
{
    // The following covers most of the Phidget types that you'll use, but
    // you may want to look at the API if there's a sensor you can't find.
    // https://www.phidgets.com/?view=api (Use C# / VB.NET for the language)
    private Encoder dial;                   // Any type of dial that "ticks" is an encoder

    private VoltageRatioInput thumbstickX;  // Many Phidgets have several sensors--they'll typically be written out
    private VoltageRatioInput thumbstickY;  // on the Phidget's casing under an OBJECTS header
    private DigitalInput thumbstickZ;

    private VoltageRatioInput turn10;  // Almost all of the sensor Phidgets (ones that look like circuit boards)
    private VoltageRatioInput slider;  // will be the VoltageRatioInput sensor type, which means they have a voltage
    private VoltageRatioInput touch;   // rating from some set number to another, typically 0 to 1 or -1 to 1.
    private VoltageRatioInput magnet;
    private VoltageRatioInput IRReflective;   //Though it's a VoltageRatioSensor type, it returns a bool value

    // These are variables used to track the state of the game. Much of the Unity functionality can't be accessed in the
    // callbacks for the Phidgets like rendering variables and transforms, so you'll have to store the result from the
    // Phidget callback function and process it later (likely inside of Update())
    private Vector2 translationChange = Vector2.zero;
    private float transformChange = 0f;

    private Vector3 currentPos = Vector3.zero;
    private float currRotation = 0f;
    private float prevRotation = 0f;
    private float currWidth = 1f;
    private float prevWidth = 1f;
    private Vector3 currScale = Vector3.one;

    private bool thumbClick = false;
    private bool isTouched = false;
    private bool isInsight = false;
    private float shakePower = 0f;

    private Material renderMat;

    // Use this for initialization
    void Start()
    {
        // Get the material from the Renderer component
        renderMat = GetComponent<Renderer>().material;

        #region device_init

        // Slider 60mm
        // NOTE: *Most* sensor Phidgets need the hub port, channel, hub port device status, and local status defined
        //       order to work. It's probably better to just be safe about it and be explicit for most Phidgets.
        slider = new VoltageRatioInput();
        slider.HubPort = 0; // Make sure you plugged the responding Phidget to the right port
        slider.Channel = 0;
        slider.IsHubPortDevice = true;
        slider.IsLocal = true;
        slider.Attach += ratioAttachCallback;              // The Attach callback is called when a device successfully attaches to
                                                           // your object after calling open() on it.
        slider.VoltageRatioChange += ratioChangeCallback;  // The Change callback is called when the device registers a change,
                                                           // which is defined by the data interval of the device. This will probably
                                                           // get called really often, so be wary of that.

        // Dial Phidget
        dial = new Encoder();
        dial.HubPort = 1;
        dial.Attach += encoderAttachCallback;
        dial.PositionChange += encoderChangeCallback;

        // Thumbstick Phidget
        // Y axis
        thumbstickY = new VoltageRatioInput();
        thumbstickY.Channel = 0;  // The Y axis is channel 0, which can be found in the Phidget Control Panel 
        thumbstickY.HubPort = 2;
        thumbstickY.Attach += ratioAttachCallback;
        thumbstickY.VoltageRatioChange += ratioChangeCallback;
        // X axis
        thumbstickX = new VoltageRatioInput();
        thumbstickX.Channel = 1;  // The X axis is channel 1, which can be found in the Phidget Control Panel 
        thumbstickX.HubPort = 2;
        thumbstickX.Attach += ratioAttachCallback;
        thumbstickX.VoltageRatioChange += ratioChangeCallback;
        // Z axis
        thumbstickZ = new DigitalInput();
        thumbstickZ.HubPort = 2;
        thumbstickZ.Attach += digitalAttachCallback;
        thumbstickZ.StateChange += digitalChangeCallback;

        // Rotation Sensor 10-turn
        turn10 = new VoltageRatioInput();
        turn10.HubPort = 3;
        turn10.Channel = 0;
        turn10.IsHubPortDevice = true;
        turn10.IsLocal = true;
        turn10.Attach += ratioAttachCallback;
        turn10.VoltageRatioChange += ratioChangeCallback;

        // Touch Sensor
        touch = new VoltageRatioInput();
        touch.HubPort = 4;
        touch.Channel = 0;
        touch.IsHubPortDevice = true;
        touch.IsLocal = true;
        touch.Attach += ratioAttachCallback;
        touch.VoltageRatioChange += ratioChangeCallback;

        // Magnetic Sensor
        magnet = new VoltageRatioInput();
        magnet.HubPort = 5;
        magnet.Channel = 0;
        magnet.IsHubPortDevice = true;
        magnet.IsLocal = true;
        magnet.Attach += ratioAttachCallback;
        magnet.VoltageRatioChange += ratioChangeCallback;

        //IR Reflective Sensor (using port 3(in switch of rotation sensor))
        IRReflective = new VoltageRatioInput { HubPort = 3, Channel = 0, IsHubPortDevice = true, IsLocal = true }; //Also considering using object initializer to shorten the lines.
        IRReflective.Attach += ratioAttachCallback;
        IRReflective.VoltageRatioChange += ratioChangeCallback;

        #endregion

        // Open all of the devices to be attached to by the physical Phidgets.
        // It's not smart to do all of this in one try-catch, but I'm just lazy.

        // ^^ That's fine, I updated it (even though I'm lazy, too) - Shawn

        #region  try_catch_for_open_device
        try
        {
            slider.Open(1000);
        }
        catch (PhidgetException e)
        {
            Debug.Log("Failed opening slider: " + e.Message);
        }
        try
        {
            dial.Open(1000);
        }
        catch (PhidgetException e)
        {
            Debug.Log("Failed opening dial: " + e.Message);
        }
        try
        {
            thumbstickX.Open(1000);
            thumbstickY.Open(1000);
            thumbstickZ.Open(1000);
        }
        catch (PhidgetException e)
        {
            Debug.Log("Failed opening thumbstick: " + e.Message);
        }
        try
        {
            touch.Open(1000);
        }
        catch (PhidgetException e)
        {
            Debug.Log("Failed opening touch: " + e.Message);
        }
        try
        {
            turn10.Open(1000);
        }
        catch (PhidgetException e)
        {
            Debug.Log("Failed opening turn10: " + e.Message);
        }
        try
        {
            magnet.Open(1000);
        }
        catch (PhidgetException e)
        {
            Debug.Log("Failed opening magnet: " + e.Message);
        }
        try
        {
            IRReflective.Open(1000);
        }
        catch (PhidgetException e)
        {
            Debug.Log("Failed opening IRReflective: " + e.Message);
        }
        #endregion

    }

    void OnDestroy()
    {
        // IMPORTANT: You must remember to close your Phidgets before ending the game! Otherwise, the next time you try to
        // grab any Phidget that was not closed, your program may freeze (the Unity editor often does).
        dial.Close();
        thumbstickX.Close();
        thumbstickY.Close();
        thumbstickZ.Close();
        touch.Close();
        slider.Close();
        turn10.Close();
        magnet.Close();
        IRReflective.Close();
    }

    // Update is called once per frame
    void Update()
    {
        // Here we process all of the data that we received from the Phidgets via their callbacks.
        // This is not good style. Each of these processes should probably be in a different function.
        currScale += Vector3.one * transformChange * Time.deltaTime;
        currentPos += new Vector3(translationChange.x, 0f, translationChange.y) * 5f * Time.deltaTime;

        transform.localPosition = currentPos;
        transform.localPosition += new Vector3(Random.value * 2f - 1f, Random.value * 2f - 1f, Random.value * 2f - 1f) * shakePower;

        transform.localScale = currScale;
        transform.localScale = new Vector3(transform.localScale.x * 2f * currWidth, transform.localScale.y, transform.localScale.z);
        transform.localScale *= thumbClick ? 2f : .5f;

        transform.localRotation = Quaternion.Euler(0f, 0f, currRotation * 360f * 10f);

        transformChange = 0f;
        translationChange = Vector2.zero;

        renderMat.color = isTouched ? Color.red : (isInsight ? Color.blue : Color.white);
    }

    // Each type usually needs to have a different callback because of different parameter types, but
    // it's also just a good idea to make different callbacks for each Phidget or set of Phidgets so that
    // you can have different attachment/detachment behaviors depending on the Phidget.
    void encoderAttachCallback(object sender, Phidget22.Events.AttachEventArgs e)
    {
        Encoder attachedDevice = (Encoder)sender;
        attachedDevice.DataInterval = attachedDevice.MinDataInterval;  // Here we set the data interval, which is the rate
                                                                       // at which the Phidget sends its data, to the minimum
                                                                       // value. You'll want to take more care to set a reasonable
                                                                       // value because frequent responses means more resources are
                                                                       // spent on retrieving those values.
        Debug.Log("Attached device " + attachedDevice.DeviceSerialNumber);
    }

    void encoderChangeCallback(object sender, Phidget22.Events.EncoderPositionChangeEventArgs e)
    {
        // With only one encoder, there's nothing really to ensure.
        transformChange = e.PositionChange;
    }

    void ratioAttachCallback(object sender, Phidget22.Events.AttachEventArgs e)
    {
        VoltageRatioInput attachedDevice = (VoltageRatioInput)sender;
        attachedDevice.DataInterval = attachedDevice.MinDataInterval;  // Setting the data interval here too.
        Debug.Log("Attached device " + attachedDevice.DeviceSerialNumber);
    }

    void ratioChangeCallback(object sender, Phidget22.Events.VoltageRatioInputVoltageRatioChangeEventArgs e)
    {
        // We have a lot of different VoltageRatioInput devices, so I'm being lazy by just checking against them
        // in the same callback. It will probably serve you better to make separate callbacks for the devices.

        // NOTE: You may notice that we're checking the data before we use it for most of the sensors. The Phidgets
        // tend to be very noisy and they don't hold a stable value, so you will probably need to similarly filter
        // your data to keep your inputs from jumping around.
        if (sender == thumbstickX)
        {
            translationChange.x += Mathf.Abs((float)e.VoltageRatio) > .035 ? (float)e.VoltageRatio : 0f;
        }
        else if (sender == thumbstickY)
        {
            translationChange.y += Mathf.Abs((float)e.VoltageRatio) > .035 ? (float)e.VoltageRatio : 0f;
        }
        else if (sender == turn10)
        {
            if (Mathf.Abs(prevRotation - (float)e.VoltageRatio) > .001f)
            {
                currRotation = (float)e.VoltageRatio;
                prevRotation = currRotation;
            }
        }
        else if (sender == slider)
        {
            if (prevWidth - (float)e.VoltageRatio > .005f)
            {
                currWidth = (float)e.VoltageRatio * .9f + .1f;
                prevWidth = currWidth;
            }
        }
        else if (sender == touch)
        {
            isTouched = e.VoltageRatio > .5;
        }
        else if (sender == magnet)
        {
            if (Mathf.Abs((float)e.VoltageRatio - .5f) > .015f)
                shakePower = Mathf.Abs((float)e.VoltageRatio - .5f) * 2f;
            else
                shakePower = 0f;
        }
        else if (sender == IRReflective)
        {
            isInsight = e.VoltageRatio < .5;
        }
    }

    void digitalAttachCallback(object sender, Phidget22.Events.AttachEventArgs e)
    {
        DigitalInput attachedDevice = (DigitalInput)sender;
        Debug.Log("Attached device " + attachedDevice.DeviceSerialNumber);
    }

    void digitalChangeCallback(object sender, Phidget22.Events.DigitalInputStateChangeEventArgs e)
    {
        thumbClick = e.State;
    }
}
