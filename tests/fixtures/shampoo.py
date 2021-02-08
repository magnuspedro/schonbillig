# @pytest.fixture
def shampoo_wella():
    name = '''<h1 class="nproduct-title">
            Wella Professionals Fusion
                <span class="product-subtitle">  - Shampoo 50ml</span>
        </h1>'''
    size = ''
    sku = '''<div class="product-sku">
                <strong>Cod: </strong>52110
            </div>'''
    infos = '''<div class="container-padding product-datasheet container-padding-top card-xs">
        <div class="accordion-gradient">
            <input type="checkbox" class="is-hide accordion-state" id="product-datasheet" checked="">
            <div class="accordion-gradient-content datasheet">
                <div class="datasheet-categories"> 
                    <span class="info-label">Categorias</span>
                    <div>
                        <span class="info-link info-link-category">
                            <a href="/cabelos" data-interaction="{&quot;category&quot;: &quot;PRODUCTS&quot;, &quot;action&quot;: &quot;Link-Click&quot;, &quot;label&quot;: &quot;datasheet department&quot;, &quot;values&quot;: &quot;department;cabelos&quot;}">
                                Cabelos
                            </a>
                        </span>
                            <span class="info-link info-link-category">
                                <a href="/cabelos/shampoo" data-interaction="{&quot;category&quot;: &quot;PRODUCTS&quot;, &quot;action&quot;: &quot;Link-Click&quot;, &quot;label&quot;: &quot;datasheet category&quot;, &quot;values&quot;: &quot;category;cabelos/shampoo&quot;}">
                                    Shampoo
                                </a>
                            </span>
                    </div>
                </div>
                <div class="datasheet-characteristics">
                            <div class="info-line">
                                <span class="info-label">Tipos de Cabelo</span>
                                            <strong class="info-link">
                                                <a href="/cabelos/shampoo/danificados" data-interaction="{&quot;category&quot;: &quot;PRODUCTS&quot;, &quot;action&quot;: &quot;Link-Click&quot;, &quot;label&quot;: &quot;datasheet attribute&quot;,  &quot;values&quot;: &quot;attribute;/cabelos/shampoo/danificados&quot;}">
                                                    Danificados
                                                </a>
                                            </strong>       
                            </div>
                            <div class="info-line">
                                <span class="info-label">Condição dos Fios</span>
                                            <strong class="info-link">
                                                <a href="/cabelos/shampoo/danificados?condicao-dos-fios=quebradicos" data-interaction="{&quot;category&quot;: &quot;PRODUCTS&quot;, &quot;action&quot;: &quot;Link-Click&quot;, &quot;label&quot;: &quot;datasheet attribute&quot;,  &quot;values&quot;: &quot;attribute;/cabelos/shampoo/danificados?condicao-dos-fios=quebradicos&quot;}">
                                                    Quebradiços
                                                </a>
                                            </strong>
                            </div>
                            <div class="info-line">
                                <span class="info-label">Desejo de Beleza</span>
                                            <span class="info-value">
                                                Força e Resistência
                                            </span>
                            </div>
                            <div class="info-line">
                                <span class="info-label">Tamanho</span>
                                            <strong class="info-link">
                                                <a href="/cabelos/shampoo/danificados?tamanho=miniatura" data-interaction="{&quot;category&quot;: &quot;PRODUCTS&quot;, &quot;action&quot;: &quot;Link-Click&quot;, &quot;label&quot;: &quot;datasheet attribute&quot;,  &quot;values&quot;: &quot;attribute;/cabelos/shampoo/danificados?tamanho=miniatura&quot;}">
                                                    Miniatura
                                                </a>
                                            </strong>
                           </div>                  
                        <div class="info-line">
                            <span class="info-label">Marca</span>
                            <strong class="info-link">
                                <a href="/wella-professionals/cabelos/shampoo" data-interaction="{&quot;category&quot;: &quot;PRODUCTS&quot;, &quot;action&quot;: &quot;Link-Click&quot;, &quot;label&quot;: &quot;datasheet brand wella-professionals/cabelos/shampoo&quot;}">
                                    Wella Professionals
                                </a>
                            </strong>
                        </div>
                        <div class="info-line">
                            <span class="info-label">Linha</span>
                            <strong class="info-link">
                                <a href="/wella-professionals/fusion" data-interaction="{&quot;category&quot;: &quot;PRODUCTS&quot;, &quot;action&quot;: &quot;Link-Click&quot;, &quot;label&quot;: &quot;datasheet brand line wella-professionals/fusion&quot;}">
                                    Fusion
                                </a>
                            </strong>
                        </div>
                </div>
            </div>
        </div>
    </div>'''
    price = '''<div class="nprodct-price">     
        <strong class="nproduct-price-max">
            <s>R$ 555.059,90</s>
<span class="" data-href="https://www.belezanaweb.com.br/wella-professionals-fusion-shampoo-50ml/">
    (17% de desconto)
</span>
        </strong>
    <div class="nproduct-price-value" content="49.9">
        R$ 555.059,90
    </div>
</div>'''
    html = name + size + sku + infos + price
    return html
