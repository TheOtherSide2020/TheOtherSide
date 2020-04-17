using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ContentListButton : MonoBehaviour
{
    public int idx;
    public TMPro.TMP_Text text;
    Button button;

    void Start()
    {
        text = GetComponentInChildren<TMPro.TMP_Text>();
        button = GetComponent<Button>();
        button.onClick.AddListener(() => OnClick(idx));
    }

    public void OnClick(int idx) {
        SelectionMenu.Instance.PreviewContent(idx);
    }
}
