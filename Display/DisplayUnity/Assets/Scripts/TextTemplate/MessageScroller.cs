using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MessageScroller : MonoBehaviour
{
    [SerializeField] List<GameObject> DisplayMsg;
    [SerializeField] List<GameObject> DisplayAnchor;

    enum ScrollingState {
        Scrolling,
        Idle
    }

    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
