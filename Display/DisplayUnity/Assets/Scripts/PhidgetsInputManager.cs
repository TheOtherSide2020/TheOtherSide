using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Phidget22;
using Phidget22.Events;
using UnityEngine.Events;

public class PhidgetsInputManager : MonoBehaviour
{
    #region Singleton
    public static PhidgetsInputManager Instance = null;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
        numberOfSensors = 0;
        sensors = new List<LightSensor>();
        portMap = new Dictionary<int, int>();
    }
    #endregion

    [SerializeField] int maxNumberOfSensors = 6;
    [SerializeField] int numberOfSensors;
    [SerializeField] float lightThreshold;
    private List<LightSensor> sensors;
    [SerializeField] List<double> lastIllum;
    private List<bool> previouslyPressed;
    private Dictionary<int, int> portMap;
    public delegate void OnIncreaseProgress(int idx);
    public delegate void OnStopProgress(int idx);
    public OnIncreaseProgress OnIncreseProgressCallback;
    public OnStopProgress OnStopProgressCallback;

    void CloseSensors() {
        // IMPORTANT: You must remember to close your Phidgets before ending the game! Otherwise, the next time you try to
        // grab any Phidget that was not closed, your program may freeze (the Unity editor often does).
        foreach (LightSensor sensor in sensors) {
            sensor.Close();
        }           
    }

    void OnDestroy()
    {
        CloseSensors();
    }

    private void Update()
    {
        // check if each sensor is activated 
        for (int i = 0; i < sensors.Count; ++i)
        {
            if (lastIllum[i] < (double)lightThreshold)
            {
                // calling on press
                OnIncreseProgressCallback?.Invoke(i);
                previouslyPressed[i] = true;
            }
            else if (previouslyPressed[i])
            {
                // calling stop
                OnStopProgressCallback?.Invoke(i);
                previouslyPressed[i] = false;
            }
        }       
    }

    void illuminanceCallback(object sender, Phidget22.Events.LightSensorIlluminanceChangeEventArgs e)
    {
        LightSensor attachedDevice = (LightSensor)sender;
        int portIdx = attachedDevice.HubPort;
        // Debug.Log(e.Illuminance);    
        // map to option index
        lastIllum[portMap[portIdx]] = e.Illuminance;
    }

    public void SetSensorPorts(int n, int[] ports) {
        // close sensors
        CloseSensors();
        // update total sensor numbers
        numberOfSensors = n;
        sensors = new List<LightSensor>();
        lastIllum = new List<double>();
        previouslyPressed = new List<bool>();
        portMap = new Dictionary<int, int>();
        for (int i = 0; i < n; ++i)
        {
            LightSensor newSensor = new LightSensor();
            newSensor.HubPort = ports[i];
            newSensor.Channel = 0;
            //lights.IsHubPortDevice = true;
            //lights.IsLocal = true;
            newSensor.IlluminanceChange += illuminanceCallback;
            sensors.Add(newSensor);
            lastIllum.Add(0);
            portMap.Add(ports[i], i);
            previouslyPressed.Add(false);
        }
        // open new sensors
        for (int i = 0; i < numberOfSensors; ++i)
        {
            try
            {
                sensors[i].Open(1000);
            }
            catch (PhidgetException e)
            {
                Debug.Log("Failed opening Light: " + i + ", " + e.Message);
            }
        }
    }

    public void SetSensorThreshold(float newValue) {
        lightThreshold = newValue;
    }
}
