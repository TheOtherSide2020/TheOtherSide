using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ContainerSizeUpdater : MonoBehaviour
{
    // Start is called before the first frame update
    [SerializeField] TMPro.TextMeshPro tmp;
    [SerializeField] RectTransform[] adjustableContainer;
    [SerializeField] List<Vector2> originalSize;
    [SerializeField] Vector2 size;
    [SerializeField] float padding = 3.5f;
    [SerializeField] bool isMainBubble = false;
    [SerializeField] bool alignMiddle = false;
    void Start()
    {
        originalSize = new List<Vector2>();
        foreach (RectTransform rt in adjustableContainer) {
            originalSize.Add(rt.sizeDelta);
        }
    }

    // Update is called once per frame
    void Update()
    {
        size =  tmp.GetPreferredValues();
        //Debug.Log(vec);
    }

    public void UpdateSize() {
        Vector2 vec = tmp.GetPreferredValues();
        // adjust background container
        adjustableContainer[0].sizeDelta = new Vector2(adjustableContainer[0].sizeDelta.x, vec.y + padding * 2);
        if (!alignMiddle) {
            Vector2 offset = (originalSize[0] - adjustableContainer[0].sizeDelta) / 2;
            adjustableContainer[0].localPosition += new Vector3(offset.x, offset.y, 0);
        }
        if (!isMainBubble) {
            // update filling
            adjustableContainer[1].sizeDelta = new Vector2(adjustableContainer[0].sizeDelta.x, vec.y + padding * 2);
            // adjust position
            if (!alignMiddle)
            {
                Vector2 offset = (originalSize[1] - adjustableContainer[1].sizeDelta) / 2;
                adjustableContainer[1].localPosition += new Vector3(offset.x, offset.y, 0);
            }
            // adjust checkmark
            Vector3 originalMark = adjustableContainer[2].position;
            adjustableContainer[2].position = new Vector3(originalMark.x, adjustableContainer[0].position.y, originalMark.z);

        }
    }
}
